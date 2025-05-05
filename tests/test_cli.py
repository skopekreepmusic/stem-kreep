from typer.testing import CliRunner
from stem_kreep.cli import app
import os
import tempfile

runner = CliRunner()

def test_analyze_command():
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        temp_file_path = temp_file.name

    try:
        result = runner.invoke(app, ["analyze", "run", "--path", temp_file_path])
        assert result.exit_code == 0
        assert f"Analyzing file: {temp_file_path}" in result.output
    finally:
        os.remove(temp_file_path)
