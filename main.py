from pathlib import Path
import os
import subprocess
import sys

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text


RAIZ = Path(__file__).parent
CODIGO_FONTE = RAIZ / "src"

console = Console()

CORES = [
    "bright_blue",
    "bright_magenta",
    "bright_cyan",
    "bright_green",
    "bright_yellow",
    "bright_red",
]


def print_code(caminho: Path, cor: str) -> None:
    codigo = caminho.read_text(encoding="utf-8")

    sintaxe = Syntax(
        codigo,
        "python",
        theme="monokai",
        line_numbers=True,
        word_wrap=True,
    )

    console.print(
        Panel(
            sintaxe,
            title=str(caminho.relative_to(RAIZ)),
            border_style=cor,
        )
    )


def run_mypy(caminho: Path, cor: str) -> None:
    ambiente = os.environ.copy()
    ambiente["PYTHONPATH"] = str(CODIGO_FONTE)

    resultado = subprocess.run(
        [
            sys.executable,
            "-m",
            "mypy",
            "--pretty",
            "--show-error-codes",
            str(caminho),
        ],
        cwd=RAIZ,
        env=ambiente,
        text=True,
        capture_output=True,
    )

    saida = resultado.stdout.strip() or resultado.stderr.strip()

    if resultado.returncode == 0:
        titulo = "mypy: OK"
        estilo_borda = "green"
        corpo = saida or "Success: no issues found"
    else:
        titulo = "mypy: ERRO"
        estilo_borda = "red"
        corpo = saida

    console.print(
        Panel(
            Text(corpo),
            title=titulo,
            border_style=estilo_borda,
        )
    )


def main() -> None:
    assuntos = sorted(
        caminho
        for caminho in CODIGO_FONTE.iterdir()
        if caminho.is_dir()
    )

    for indice, assunto in enumerate(assuntos):
        cor = CORES[indice % len(CORES)]

        if indice > 0:
            console.print()
            console.print()

        console.rule(
            f"[bold {cor}] {assunto.name.upper()} [/]",
            style=cor,
        )

        console.print()

        arquivo_fonte = assunto / "src_file.py"

        if arquivo_fonte.exists():
            print_code(arquivo_fonte, cor)

        diretorio_exemplos = assunto / "examples"

        arquivos_exemplo = sorted(diretorio_exemplos.glob("*.py"))

        for arquivo_exemplo in arquivos_exemplo:
            console.print()

            console.rule(
                f"[{cor}]{arquivo_exemplo.name}[/]",
                style=cor,
            )

            console.print()

            print_code(arquivo_exemplo, cor)
            run_mypy(arquivo_exemplo, cor)


if __name__ == "__main__":
    main()