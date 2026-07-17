#!/usr/bin/env python3

"""
Orquestrador principal d'IA-Productiva.

Executa, en ordre:

1. project-runner.py
2. task-builder.py
3. valida els fitxers generats
4. mostra la tasca preparada

Aquest script encara no executa cap model d'IA.
Prepara el projecte perquè el següent adaptador pugui enviar la tasca
a Claude Code, Codex o una altra IA.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


SCRIPT_DIRECTORY = Path(__file__).resolve().parent
PROJECT_RUNNER = SCRIPT_DIRECTORY / "project-runner.py"
TASK_BUILDER = SCRIPT_DIRECTORY / "task-builder.py"


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Prepara automàticament el context i la següent tasca "
            "d'un projecte compatible amb IA-Productiva."
        )
    )

    parser.add_argument(
        "project_path",
        type=Path,
        help="Camí complet o relatiu del projecte.",
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


def validate_framework_scripts() -> None:
    required_scripts = (
        PROJECT_RUNNER,
        TASK_BUILDER,
    )

    missing_scripts = [
        script for script in required_scripts if not script.is_file()
    ]

    if missing_scripts:
        missing_list = "\n".join(
            f"- {script}" for script in missing_scripts
        )

        raise FileNotFoundError(
            "Falten scripts obligatoris:\n"
            f"{missing_list}"
        )


def run_script(
    script_path: Path,
    project_path: Path,
) -> None:
    command = [
        sys.executable,
        str(script_path),
        str(project_path),
    ]

    print()
    print(f"Executant: {script_path.name}")
    print("-" * 60)

    result = subprocess.run(
        command,
        check=False,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"El script `{script_path.name}` ha fallat "
            f"amb el codi {result.returncode}."
        )


def validate_generated_files(
    project_path: Path,
) -> tuple[Path, Path]:
    output_directory = project_path / ".ia-productiva"
    context_path = output_directory / "context.md"
    task_path = output_directory / "task.md"

    required_files = (
        context_path,
        task_path,
    )

    missing_files = [
        path for path in required_files if not path.is_file()
    ]

    if missing_files:
        missing_list = "\n".join(
            f"- {path}" for path in missing_files
        )

        raise FileNotFoundError(
            "No s'han generat tots els fitxers esperats:\n"
            f"{missing_list}"
        )

    if context_path.stat().st_size == 0:
        raise ValueError(
            f"El fitxer de context està buit: {context_path}"
        )

    if task_path.stat().st_size == 0:
        raise ValueError(
            f"El fitxer de tasca està buit: {task_path}"
        )

    return context_path, task_path


def extract_active_task(task_path: Path) -> str:
    content = task_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    for index, line in enumerate(lines):
        if line.strip() != "## Tasca activa":
            continue

        for following_line in lines[index + 1:]:
            candidate = following_line.strip()

            if candidate:
                return candidate

    return "No s'ha pogut identificar la tasca activa."


def print_summary(
    project_path: Path,
    context_path: Path,
    task_path: Path,
    active_task: str,
) -> None:
    print()
    print("=" * 60)
    print("PROJECTE PREPARAT")
    print("=" * 60)
    print(f"Projecte: {project_path.name}")
    print(f"Camí: {project_path}")
    print(f"Tasca activa: {active_task}")
    print(f"Context: {context_path}")
    print(f"Instrucció: {task_path}")
    print()
    print(
        "El projecte ja està preparat perquè un adaptador "
        "l'enviï a una IA."
    )


def main() -> int:
    arguments = parse_arguments()

    try:
        project_path = validate_project_path(
            arguments.project_path
        )

        validate_framework_scripts()

        run_script(
            script_path=PROJECT_RUNNER,
            project_path=project_path,
        )

        run_script(
            script_path=TASK_BUILDER,
            project_path=project_path,
        )

        context_path, task_path = validate_generated_files(
            project_path
        )

        active_task = extract_active_task(task_path)

        print_summary(
            project_path=project_path,
            context_path=context_path,
            task_path=task_path,
            active_task=active_task,
        )

        return 0

    except (
        FileNotFoundError,
        NotADirectoryError,
        RuntimeError,
        ValueError,
        OSError,
    ) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())