#!/usr/bin/env python3

"""
Project Runner d'IA-Productiva.

Carrega el context principal d'un projecte, detecta la següent tasca pendent
i genera un paquet de context preparat perquè qualsevol IA pugui treballar-hi.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path


DOCUMENT_CANDIDATES: dict[str, tuple[str, ...]] = {
    "Regles del projecte": (
        "PROJECT_RULES.md",
        "project-rules.md",
        "project_rules.md",
    ),
    "Definició del projecte": (
        "PROJECT.md",
        "project.md",
    ),
    "Sessió actual": (
        "SESSION.md",
        "session.md",
    ),
    "Tasques pendents": (
        "TODO.md",
        "todo.md",
    ),
    "Roadmap": (
        "ROADMAP.md",
        "roadmap.md",
    ),
    "Arquitectura": (
        "docs/architecture.md",
    ),
    "Context del framework": (
        "docs/framework-context.md",
    ),
}


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Carrega el context d'un projecte i genera un paquet de treball "
            "compatible amb IA-Productiva."
        )
    )

    parser.add_argument(
        "project_path",
        type=Path,
        help="Camí complet o relatiu del projecte que s'ha de processar.",
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
            f"El camí indicat no és una carpeta: {resolved_path}"
        )

    return resolved_path


def find_document(
    project_path: Path,
    candidates: tuple[str, ...],
) -> Path | None:
    for candidate in candidates:
        document_path = project_path / candidate

        if document_path.is_file():
            return document_path

    return None


def read_document(document_path: Path) -> str:
    try:
        return document_path.read_text(encoding="utf-8").strip()
    except UnicodeDecodeError as error:
        raise ValueError(
            f"No s'ha pogut llegir com a UTF-8: {document_path}"
        ) from error


def load_project_documents(
    project_path: Path,
) -> dict[str, tuple[Path, str]]:
    loaded_documents: dict[str, tuple[Path, str]] = {}

    for section_name, candidates in DOCUMENT_CANDIDATES.items():
        document_path = find_document(project_path, candidates)

        if document_path is None:
            continue

        loaded_documents[section_name] = (
            document_path,
            read_document(document_path),
        )

    return loaded_documents


def find_next_task(todo_content: str) -> str | None:
    unchecked_task_pattern = re.compile(
        r"^\s*[-*]\s+\[\s\]\s+(.+?)\s*$",
        re.MULTILINE,
    )

    match = unchecked_task_pattern.search(todo_content)

    if match is None:
        return None

    return match.group(1).strip()


def get_todo_content(
    loaded_documents: dict[str, tuple[Path, str]],
) -> str:
    todo_document = loaded_documents.get("Tasques pendents")

    if todo_document is None:
        return ""

    return todo_document[1]


def build_context_package(
    project_path: Path,
    loaded_documents: dict[str, tuple[Path, str]],
    next_task: str | None,
) -> str:
    generated_at = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )

    sections: list[str] = [
        "# Paquet de context d'IA-Productiva",
        "",
        "## Metadades",
        "",
        f"- Projecte: `{project_path.name}`",
        f"- Camí: `{project_path}`",
        f"- Generat: `{generated_at}`",
        "",
        "## Següent tasca detectada",
        "",
        (
            f"- [ ] {next_task}"
            if next_task
            else "No s'ha detectat cap tasca pendent amb el format `- [ ]`."
        ),
        "",
        "## Instruccions per a la IA",
        "",
        "1. Respecta les regles i l'arquitectura carregades.",
        "2. Treballa únicament sobre la següent tasca pendent.",
        "3. No modifiquis l'estructura sense una decisió documentada.",
        "4. No inventis requisits absents.",
        "5. Genera canvis petits, verificables i mantenibles.",
        "6. Indica els fitxers creats o modificats.",
        "7. No marquis la tasca com a completada sense validar-la.",
        "",
    ]

    for section_name, (document_path, content) in loaded_documents.items():
        relative_path = document_path.relative_to(project_path)

        sections.extend(
            [
                "---",
                "",
                f"## {section_name}",
                "",
                f"Font: `{relative_path}`",
                "",
                content or "_Document buit._",
                "",
            ]
        )

    return "\n".join(sections).rstrip() + "\n"


def save_context_package(
    project_path: Path,
    context_content: str,
) -> Path:
    output_directory = project_path / ".ia-productiva"
    output_directory.mkdir(parents=True, exist_ok=True)

    output_path = output_directory / "context.md"
    output_path.write_text(context_content, encoding="utf-8")

    return output_path


def main() -> int:
    arguments = parse_arguments()

    try:
        project_path = validate_project_path(arguments.project_path)
        loaded_documents = load_project_documents(project_path)

        if not loaded_documents:
            print(
                "Error: no s'ha trobat cap document de projecte compatible.",
                file=sys.stderr,
            )
            return 1

        todo_content = get_todo_content(loaded_documents)
        next_task = find_next_task(todo_content)

        context_content = build_context_package(
            project_path=project_path,
            loaded_documents=loaded_documents,
            next_task=next_task,
        )

        output_path = save_context_package(
            project_path=project_path,
            context_content=context_content,
        )

        print("Context generat correctament.")
        print(f"Projecte: {project_path}")
        print(f"Documents carregats: {len(loaded_documents)}")
        print(
            f"Següent tasca: {next_task or 'cap tasca detectada'}"
        )
        print(f"Fitxer generat: {output_path}")

        return 0

    except (FileNotFoundError, NotADirectoryError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"Error del sistema: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())