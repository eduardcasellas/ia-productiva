#!/usr/bin/env python3

"""
Adaptador d'IA per a IA-Productiva.

Envia el fitxer `.ia-productiva/task.md` a Claude Code o Codex
en mode no interactiu, executant la IA dins del projecte objectiu.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


SUPPORTED_PROVIDERS = ("claude", "codex")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Executa la tasca preparada per IA-Productiva "
            "amb Claude Code o Codex."
        )
    )

    parser.add_argument(
        "project_path",
        type=Path,
        help="Camí complet o relatiu del projecte.",
    )

    parser.add_argument(
        "--provider",
        choices=SUPPORTED_PROVIDERS,
        required=True,
        help="IA que executarà la tasca.",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mostra l'ordre sense executar-la.",
    )

    return parser.parse_args()


def validate_project_path(project_path: Path) -> Path:
    resolved_path = project_path.expanduser().resolve()

    if not resolved_path.exists():
        raise FileNotFoundError(
            f"El projecte no existeix: {resolved_path}"
        )

    if not resolved_path.is_dir():
        raise NotADirectoryError(
            f"El camí no és una carpeta: {resolved_path}"
        )

    return resolved_path


def get_task_path(project_path: Path) -> Path:
    task_path = project_path / ".ia-productiva" / "task.md"

    if not task_path.is_file():
        raise FileNotFoundError(
            "No existeix `.ia-productiva/task.md`. "
            "Executa primer `run-project.py`."
        )

    if task_path.stat().st_size == 0:
        raise ValueError(
            f"El fitxer de tasca està buit: {task_path}"
        )

    return task_path


def read_task(task_path: Path) -> str:
    return task_path.read_text(encoding="utf-8").strip()


def validate_provider(provider: str) -> str:
    executable = shutil.which(provider)

    if executable is None:
        raise FileNotFoundError(
            f"No s'ha trobat l'ordre `{provider}` al sistema."
        )

    return executable


def build_command(
    provider: str,
    executable: str,
    task_content: str,
) -> list[str]:
    if provider == "claude":
        return [
            executable,
            "-p",
            "--max-turns",
            "20",
            task_content,
        ]

    if provider == "codex":
        return [
            executable,
            "exec",
            "--sandbox",
            "workspace-write",
            task_content,
        ]

    raise ValueError(
        f"Proveïdor no compatible: {provider}"
    )


def save_output(
    project_path: Path,
    provider: str,
    output: str,
) -> Path:
    output_directory = project_path / ".ia-productiva"
    output_path = output_directory / f"{provider}-output.md"

    output_path.write_text(
        output.strip() + "\n",
        encoding="utf-8",
    )

    return output_path


def run_provider(
    command: list[str],
    project_path: Path,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=project_path,
        text=True,
        capture_output=True,
        check=False,
    )


def print_dry_run(
    provider: str,
    project_path: Path,
    task_path: Path,
    command: list[str],
) -> None:
    print("Execució simulada.")
    print(f"Proveïdor: {provider}")
    print(f"Projecte: {project_path}")
    print(f"Tasca: {task_path}")
    print(f"Executable: {command[0]}")
    print()
    print("No s'ha executat cap IA.")


def main() -> int:
    arguments = parse_arguments()

    try:
        project_path = validate_project_path(
            arguments.project_path
        )

        task_path = get_task_path(project_path)
        task_content = read_task(task_path)

        executable = validate_provider(
            arguments.provider
        )

        command = build_command(
            provider=arguments.provider,
            executable=executable,
            task_content=task_content,
        )

        if arguments.dry_run:
            print_dry_run(
                provider=arguments.provider,
                project_path=project_path,
                task_path=task_path,
                command=command,
            )
            return 0

        print(
            f"Executant {arguments.provider} "
            f"sobre `{project_path.name}`..."
        )

        result = run_provider(
            command=command,
            project_path=project_path,
        )

        combined_output = "\n".join(
            part
            for part in (
                result.stdout.strip(),
                result.stderr.strip(),
            )
            if part
        )

        output_path = save_output(
            project_path=project_path,
            provider=arguments.provider,
            output=combined_output,
        )

        if result.returncode != 0:
            print(
                f"Error: {arguments.provider} ha finalitzat "
                f"amb el codi {result.returncode}.",
                file=sys.stderr,
            )
            print(f"Sortida desada a: {output_path}")
            return result.returncode

        print("Execució completada.")
        print(f"Sortida desada a: {output_path}")

        return 0

    except (
        FileNotFoundError,
        NotADirectoryError,
        ValueError,
        OSError,
    ) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())