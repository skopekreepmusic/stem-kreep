# This is the entry point for the CLI application.
import typer

app = typer.Typer()

@app.command()
def analyze(
    path: str = typer.Option(..., "--path", "-p", help="Path to the audio file to analyze")
):
    """
    Analyze an audio file.
    """
    typer.echo(f"Analyzing file: {path}")

def main():
    app()  # This is the actual CLI runner

if __name__ == "__main__":
    main()
