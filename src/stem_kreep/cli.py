import typer

app = typer.Typer()

@app.command()
def analyze(path: str):
    """
    Analyze an audio file.
    """
    typer.echo(f"Analyzing file: {path}")

if __name__ == "__main__":
    app()
