#!/usr/bin/env python3

"""
Genera una instrucció executable a partir del context creat per project-runner.py.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera el fitxer de tasca d'IA-Productiva."
    )

    parser.add_argument(
        "project_path",
        type=Path,
        help="Camí del projecte que s'ha de processar.",
    )

    return parser.parse_args()


def validate_project_path(project_path: Path) -> Path:
    resolved_path = project_path.expanduser().resolve()

    if not resolved_path.is_dir():
        raise NotADirectoryError(
            f"El projecte no existeix o no és una carpeta: {resolved_path}"
        )

    return resolved_path


def read_context(project_path: Path) -> str:
    context_path = project_path / ".ia-productiva" / "context.md"

    if not context_path.is_file():
        raise FileNotFoundError(
            "No existeix `.ia-productiva/context.md`. "
            "Executa primer `project-runner.py`."
        )

    return context_path.read_text(encoding="utf-8")


def extract_next_task(context_content: str) -> str:
    pattern = re.compile(
        r"## Següent tasca detectada\s+"
        r"- \[ \] (.+?)\s+"
        r"## Instruccions per a la IA",
        re.DOTALL,
    )

    match = pattern.search(context_content)

    if match is None:
        raise ValueError(
            "No s'ha pogut extreure una tasca pendent del context."
        )

    return match.group(1).strip()


def build_task_document(
    project_path: Path,
    task: str,
    context_content: str,
) -> str:
    return f"""# Tasca d'IA-Productiva

## Projecte

`{project_path.name}`

## Tasca activa

{task}

## Objectiu

Executar únicament aquesta tasca respectant el context, les regles i
l'arquitectura del projecte.

## Instruccions obligatòries

1. Analitza el context complet abans de modificar fitxers.
2. No executis tasques addicionals.
3. No canviïs l'estructura sense justificació.
4. Reutilitza els components i les dades existents.
5. No inventis requisits.
6. Indica tots els fitxers creats o modificats.
7. Proporciona el contingut complet dels fitxers.
8. Defineix una validació concreta.
9. No marquis la tasca com a completada fins que la validació sigui correcta.

## Format de resposta esperat

### Anàlisi breu

- Estat actual.
- Fitxers afectats.
- Riscos o dependències.

### Implementació

Per cada fitxer:

1. Camí complet.
2. Contingut complet.
3. Finalitat del canvi.

### Validació

- Ordres que s'han d'executar.
- Resultat esperat.
- Comprovació manual necessària.

## Context complet

{context_content}
"""


def save_task_document(
    project_path: Path,
    task_document: str,
) -> Path:
    output_path = project_path / ".ia-productiva" / "task.md"
    output_path.write_text(task_document, encoding="utf-8")

    return output_path


def main() -> int:
    arguments = parse_arguments()

    try:
        project_path = validate_project_path(arguments.project_path)
        context_content = read_context(project_path)
        task = extract_next_task(context_content)

        task_document = build_task_document(
            project_path=project_path,
            task=task,
            context_content=context_content,
        )

        output_path = save_task_document(
            project_path=project_path,
            task_document=task_document,
        )

        print("Tasca preparada correctament.")
        print(f"Projecte: {project_path}")
        print(f"Tasca: {task}")
        print(f"Fitxer generat: {output_path}")

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