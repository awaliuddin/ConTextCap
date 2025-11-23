# Developer Guide

Welcome to the ConTextCap Developer Guide! This document will help you get started with developing and contributing to ConTextCap.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Development Setup](#development-setup)
3. [Project Structure](#project-structure)
4. [Coding Standards](#coding-standards)
5. [Testing](#testing)
6. [Building and Packaging](#building-and-packaging)
7. [Continuous Integration](#continuous-integration)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- pip (Python package installer)
- Virtual environment tool (venv, virtualenv, or conda)

### Development Setup

1. **Fork and Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/ConTextCap.git
cd ConTextCap
```

2. **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
# Install core dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Install the package in editable mode
pip install -e .
```

4. **Set Up Pre-commit Hooks**

```bash
pre-commit install
```

This will automatically run code formatters and linters before each commit.

## Project Structure

```
ConTextCap/
├── .github/                 # GitHub workflows and templates
│   ├── workflows/          # GitHub Actions CI/CD
│   ├── ISSUE_TEMPLATE/     # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                   # Documentation
├── fonts/                  # Font files for PDF generation
├── icons/                  # Icon assets
│   ├── classic/
│   ├── vivid/
│   ├── high-contrast/
│   └── square-o/
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_icon_config.py
│   └── test_file_operations.py
├── ConTextCap.py          # Main application
├── setup.py               # Package setup script
├── pyproject.toml         # Project configuration
├── requirements.txt       # Core dependencies
├── requirements-dev.txt   # Development dependencies
└── README.md             # Project README

```

## Coding Standards

ConTextCap follows strict coding standards to ensure code quality and consistency.

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use [Black](https://black.readthedocs.io/) for code formatting (line length: 88)
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Maximum line length: 88 characters
- Maximum function complexity: 10 (McCabe)

### Code Formatting

We use automated tools to maintain code quality:

```bash
# Format code with Black
black .

# Sort imports with isort
isort .

# Lint with flake8
flake8 .

# Type check with mypy
mypy ConTextCap.py

# Security check with bandit
bandit -r .
```

### Documentation

- Use Google-style docstrings
- Document all public classes, methods, and functions
- Include type hints where appropriate
- Keep documentation up-to-date with code changes

Example:

```python
def generate_pdf(output_path: Path, content: str) -> bool:
    """
    Generate a PDF document from the provided content.

    Args:
        output_path: Path where the PDF will be saved
        content: Text content to include in the PDF

    Returns:
        True if successful, False otherwise

    Raises:
        IOError: If the output path is not writable
    """
    pass
```

## Testing

ConTextCap uses pytest for testing with comprehensive coverage requirements.

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_icon_config.py

# Run tests in parallel
pytest -n auto
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Name test functions as `test_*`
- Use fixtures from `conftest.py`
- Aim for >80% code coverage

Example:

```python
def test_icon_config_default_style():
    """Test that default icon style is set correctly."""
    config = IconConfig()
    assert config.current_style == 'high-contrast'
```

### Test Organization

- `tests/conftest.py`: Shared fixtures and configuration
- `tests/test_icon_config.py`: Icon configuration tests
- `tests/test_file_operations.py`: File operation tests

## Building and Packaging

### Building the Package

```bash
# Build source distribution and wheel
python -m build

# The built packages will be in dist/
```

### Local Installation

```bash
# Install in editable mode
pip install -e .

# Install from built package
pip install dist/contextcap-*.whl
```

## Continuous Integration

ConTextCap uses GitHub Actions for CI/CD:

### Workflows

1. **CI (ci.yml)**: Runs tests on multiple Python versions and OS
2. **Code Review (code-review.yml)**: Automated code quality checks
3. **PR Labeler (pr-labeler.yml)**: Auto-labels pull requests
4. **Security (security.yml)**: Security vulnerability scanning
5. **Documentation (docs.yml)**: Builds and deploys documentation
6. **Release (release.yml)**: Automated releases on tags

### Running CI Locally

Before pushing, ensure all checks pass:

```bash
# Run linting
flake8 .

# Run formatting check
black --check .
isort --check-only .

# Run type checking
mypy ConTextCap.py

# Run tests
pytest

# Run security checks
bandit -r .
safety check
```

## Making Changes

### Workflow

1. Create a new branch for your changes
2. Make your changes and write tests
3. Run all tests and linting
4. Commit your changes (pre-commit hooks will run)
5. Push to your fork
6. Open a pull request

### Commit Messages

Follow the conventional commits format:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Build process or auxiliary tool changes

Example:
```
feat: Add support for custom PDF templates

- Implement template selection UI
- Add template rendering logic
- Update documentation
```

## Getting Help

- Check existing [issues](https://github.com/awaliuddin/ConTextCap/issues)
- Start a [discussion](https://github.com/awaliuddin/ConTextCap/discussions)
- Read the [Contributing Guide](../CONTRIBUTING.md)

## Resources

- [Python Documentation](https://docs.python.org/3/)
- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [FPDF2 Documentation](https://py-pdf.github.io/fpdf2/)
- [pytest Documentation](https://docs.pytest.org/)

---

Thank you for contributing to ConTextCap! 🚀
