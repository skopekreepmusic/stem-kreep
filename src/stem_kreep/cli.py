# This is the entry point for the CLI application.
import typer
from stem_kreep.commands.analyze import run_analyze

app = typer.Typer(help="Stem-Kreep: A tool for analyzing and processing audio files.")

# Update the analyze subcommand to use the imported function
analyze_app = typer.Typer(help="Commands for analyzing audio files.")
analyze_app.command(name="run", help="Analyze a specific audio file.")(run_analyze)
app.add_typer(analyze_app, name="analyze")

def main():
    app()  # This is the actual CLI runner

if __name__ == "__main__":
    main()
