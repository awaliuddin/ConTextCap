"""
Pytest configuration and fixtures for ConTextCap tests.
"""
import pytest
import sys
from pathlib import Path

# Add the parent directory to the path so we can import ConTextCap
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture(scope='session')
def qapp():
    """Create a QApplication instance for testing."""
    from PyQt6.QtWidgets import QApplication
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app
    # Don't quit the app as it might be used by other tests


@pytest.fixture
def temp_dir(tmp_path):
    """Provide a temporary directory for test files."""
    return tmp_path


@pytest.fixture
def sample_project_structure(tmp_path):
    """Create a sample project structure for testing."""
    # Create directories
    (tmp_path / "src").mkdir()
    (tmp_path / "tests").mkdir()
    (tmp_path / "docs").mkdir()
    (tmp_path / ".git").mkdir()
    (tmp_path / "__pycache__").mkdir()

    # Create files
    (tmp_path / "README.md").write_text("# Sample Project\n\nThis is a sample.")
    (tmp_path / "src" / "main.py").write_text("def main():\n    print('Hello')\n")
    (tmp_path / "src" / "utils.py").write_text("def util_func():\n    return True\n")
    (tmp_path / "tests" / "test_main.py").write_text("def test_main():\n    assert True\n")
    (tmp_path / "requirements.txt").write_text("pytest\n")

    return tmp_path
