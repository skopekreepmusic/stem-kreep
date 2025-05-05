from typer.testing import CliRunner
from stem_kreep.cli import app

runner = CliRunner()

def test_analyze_command():
    result = runner.invoke(app, ["analyze", "dummy.wav"])
    assert result.exit_code == 0
    assert "Analyzing file: dummy.wav" in result.output
