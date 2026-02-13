from pathlib import Path
import subprocess
import sys


def test_create_ch1_venv(tmp_path):
    venv_dir = tmp_path / "ch1_test_env"
    python = sys.executable
    subprocess.check_call([python, "-m", "venv", str(venv_dir)])
    py_exec = venv_dir / "bin" / "python"
    assert py_exec.exists()
    repo_root = Path(__file__).resolve().parents[1]
    req = repo_root / "ch1_requirements.txt"
    assert req.exists()
