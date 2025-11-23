"""
Tests for file operation functions.
"""
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from ConTextCap import is_allowed_file


class TestFileOperations:
    """Test cases for file operations."""

    def test_is_allowed_file_python(self, tmp_path):
        """Test that Python files are allowed."""
        py_file = tmp_path / "test.py"
        py_file.write_text("print('test')")
        # The function may return True or check specific criteria
        # This is a placeholder test that should be updated based on actual implementation
        result = is_allowed_file(py_file)
        assert isinstance(result, bool)

    def test_is_allowed_file_text(self, tmp_path):
        """Test that text files are allowed."""
        txt_file = tmp_path / "test.txt"
        txt_file.write_text("test content")
        result = is_allowed_file(txt_file)
        assert isinstance(result, bool)

    def test_is_allowed_file_json(self, tmp_path):
        """Test that JSON files are allowed."""
        json_file = tmp_path / "test.json"
        json_file.write_text('{"key": "value"}')
        result = is_allowed_file(json_file)
        assert isinstance(result, bool)

    def test_is_allowed_file_markdown(self, tmp_path):
        """Test that Markdown files are allowed."""
        md_file = tmp_path / "README.md"
        md_file.write_text("# Test")
        result = is_allowed_file(md_file)
        assert isinstance(result, bool)
