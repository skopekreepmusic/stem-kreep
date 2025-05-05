# This is the entry point for the CLI application.
import typer

app = typer.Typer(help="Stem-Kreep: A tool for analyzing and processing audio files.")

# Create a sub-typer app for analyze
analyze_app = typer.Typer(help="Commands for analyzing audio files.")
app.add_typer(analyze_app, name="analyze")

@analyze_app.command(name="run", help="Analyze a specific audio file.")
def run_analyze(
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
