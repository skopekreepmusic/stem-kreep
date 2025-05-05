import os
import typer

def run_analyze(
    path: str = typer.Option(..., "--path", "-p", help="Path to the audio file to analyze")
):
    """
    Analyze an audio file.
    """
    if not os.path.exists(path):
        typer.echo(f"Error: File '{path}' does not exist.", err=True)
        raise typer.Exit(code=2)

    typer.echo(f"Analyzing file: {path}")