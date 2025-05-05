import typer

def run_analyze(
    path: str = typer.Option(..., "--path", "-p", help="Path to the audio file to analyze")
):
    """
    Analyze an audio file.
    """
    typer.echo(f"Analyzing file: {path}")