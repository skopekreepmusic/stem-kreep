"""Console script for stem_kreep."""
import stem_kreep

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for stem_kreep."""
    console.print("Replace this message by putting your code into "
               "stem_kreep.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
