<div align="center">

# ConTextCap 📚

### Context Capture for Modern Developers

[![GitHub license](https://img.shields.io/github/license/awaliuddin/ConTextCap)](https://github.com/awaliuddin/ConTextCap/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/badge/pypi-v1.0.0-blue?logo=pypi&logoColor=white)](https://pypi.org/project/contextcap/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![CI](https://github.com/awaliuddin/ConTextCap/workflows/CI/badge.svg)](https://github.com/awaliuddin/ConTextCap/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/awaliuddin/ConTextCap/branch/main/graph/badge.svg)](https://codecov.io/gh/awaliuddin/ConTextCap)
[![Security](https://github.com/awaliuddin/ConTextCap/workflows/Security/badge.svg)](https://github.com/awaliuddin/ConTextCap/actions/workflows/security.yml)
[![Documentation](https://github.com/awaliuddin/ConTextCap/workflows/Documentation/badge.svg)](https://github.com/awaliuddin/ConTextCap/actions/workflows/docs.yml)

[![GitHub stars](https://img.shields.io/github/stars/awaliuddin/ConTextCap?style=social)](https://github.com/awaliuddin/ConTextCap/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/awaliuddin/ConTextCap?style=social)](https://github.com/awaliuddin/ConTextCap/network)
[![GitHub issues](https://img.shields.io/github/issues/awaliuddin/ConTextCap)](https://github.com/awaliuddin/ConTextCap/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/awaliuddin/ConTextCap)](https://github.com/awaliuddin/ConTextCap/pulls)
[![Contributors](https://img.shields.io/github/contributors/awaliuddin/ConTextCap)](https://github.com/awaliuddin/ConTextCap/graphs/contributors)

**Transform your entire codebase into a single, beautiful PDF document perfect for LLMs, code reviews, and documentation.**

[📖 Documentation](docs/) • [🚀 Getting Started](#installation) • [💡 Examples](#usage) • [🤝 Contributing](CONTRIBUTING.md) • [🐛 Report Bug](https://github.com/awaliuddin/ConTextCap/issues/new?template=bug_report.md) • [✨ Request Feature](https://github.com/awaliuddin/ConTextCap/issues/new?template=feature_request.md)

</div>

---

## 🌟 Why ConTextCap?

ConTextCap (Context Capture) is your ultimate tool for capturing and documenting entire codebases. Whether you're:

- 🤖 **Working with LLMs**: Feed your entire codebase to ChatGPT, Claude, or other AI assistants
- 📚 **Creating Documentation**: Generate comprehensive project snapshots
- 👥 **Onboarding Developers**: Help new team members understand the codebase quickly
- 🔍 **Code Reviews**: Share entire project context in a single, portable document
- 📦 **Archiving Projects**: Create historical snapshots of your codebase

ConTextCap makes it effortless!

## ✨ Key Features

### Core Capabilities

| Feature | Description |
|---------|-------------|
| 🌳 **Directory Tree Visualization** | Beautiful hierarchical view of your project structure |
| 📄 **Complete Code Capture** | Full content of text files (Python, JS, JSON, Markdown, etc.) |
| 📊 **Binary File Handling** | Smart metadata display for non-text files |
| 🎨 **Multiple Icon Styles** | Classic, Vivid, High-Contrast, and Square-O themes |
| 🔍 **Intelligent Filtering** | Auto-excludes `.git`, `node_modules`, `__pycache__`, etc. |
| 📱 **Modern PyQt6 UI** | Clean, intuitive, and responsive interface |
| 📈 **Progress Tracking** | Real-time progress for large projects |
| 🔒 **100% Offline** | No internet required, your code stays private |
| 🚀 **Fast Processing** | Optimized for projects with thousands of files |
| 🎯 **Production Ready** | Comprehensive testing, CI/CD, and quality checks |

### Supported File Types

**Text Files** (Full Content):
- **Languages**: `.py`, `.js`, `.ts`, `.java`, `.cpp`, `.c`, `.go`, `.rs`, `.rb`, `.php`
- **Web**: `.html`, `.css`, `.scss`, `.jsx`, `.tsx`, `.vue`
- **Data**: `.json`, `.xml`, `.yaml`, `.yml`, `.toml`, `.csv`
- **Docs**: `.md`, `.rst`, `.txt`, `.log`
- **Config**: `.ini`, `.conf`, `.cfg`, `.env.example`

**Binary Files** (Metadata Only):
- File size, type, and path information

## 🚀 Quick Start

### Installation

#### Option 1: Install via pip (Recommended)

```bash
pip install contextcap
```

#### Option 2: Install from Source

```bash
# Clone the repository
git clone https://github.com/awaliuddin/ConTextCap.git
cd ConTextCap

# Install dependencies
pip install -r requirements.txt

# Optional: Install in development mode
pip install -e ".[dev]"
```

### Prerequisites

- **Python**: 3.8 or higher
- **OS**: Windows, macOS, or Linux
- **Dependencies**: Automatically installed with pip

## 💡 Usage

### GUI Application

1. **Launch ConTextCap:**
   ```bash
   # If installed via pip
   contextcap

   # If running from source
   python ConTextCap.py
   ```

2. **Generate Your PDF:**
   - Click **"Select Directory"** and choose your project
   - Pick your preferred **icon style** (Classic, Vivid, High-Contrast, or Square-O)
   - Click **"Generate PDF"** and choose where to save
   - Wait for completion and enjoy your PDF!

### Command Line (Coming Soon)

```bash
# Generate PDF from command line
contextcap --input ./my-project --output ./docs/project.pdf --style vivid

# Batch processing
contextcap --batch projects.txt

# Custom exclusions
contextcap --input ./src --exclude "*.log,*.tmp,test_*"
```

### Example Use Cases

#### 1. Feed Your Codebase to an LLM

```python
# After generating your PDF, simply upload it to:
# - ChatGPT (with PDF support)
# - Claude (via artifact)
# - Other LLM tools

# The PDF contains your complete codebase in a format
# that's perfect for AI analysis and assistance
```

#### 2. Code Review Package

```bash
# Generate a comprehensive code review document
contextcap --input ./feature-branch --output ./review.pdf

# Share review.pdf with your team
```

#### 3. Project Documentation Snapshot

```bash
# Create a snapshot before major refactoring
contextcap --input ./src --output ./snapshots/v1.0-snapshot.pdf
```

## Features in Detail 🔍

### Directory Tree 🌳
The application generates a hierarchical view of your project's structure, making it easy to understand the organization of your codebase.

### File Content Processing 📝
- **Text Files**: Full content is included in the PDF
  - Supported formats: `.py`, `.js`, `.json`, `.xml`, `.md`, `.txt`, `.rst`, `.log`, `.ini`, `.conf`, `.cfg`
- **Binary Files**: File information (size, type) is displayed
- **Special Handling**: Unicode characters are properly handled and converted

### User Interface 🎨
- Clean and intuitive design
- Progress tracking for large projects
- Error handling with user-friendly messages
- Persistent settings for user preferences

## 🏗️ Architecture

ConTextCap is built with modern Python development practices:

```
ConTextCap/
├── 🎨 PyQt6 UI Layer          # Modern, responsive interface
├── 📄 FPDF2 Engine            # High-quality PDF generation
├── 🔧 Icon System             # Modular, themeable icons
├── 🧪 Comprehensive Tests     # pytest with >80% coverage
├── 🔄 CI/CD Pipeline          # Automated testing and deployment
└── 📚 Rich Documentation      # User and developer guides
```

### Tech Stack

- **UI Framework**: PyQt6
- **PDF Generation**: fpdf2
- **Testing**: pytest, pytest-qt, pytest-cov
- **Code Quality**: black, isort, flake8, mypy, bandit
- **CI/CD**: GitHub Actions
- **Documentation**: Sphinx, pdoc3

## 🤝 Contributing

We **love** contributions from the community! Whether you're:

- 🐛 Reporting bugs
- 💡 Suggesting features
- 📝 Improving documentation
- 🔧 Submitting code
- ⭐ Starring the repo

Every contribution matters! 🎉

### Quick Contribution Guide

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ConTextCap.git
cd ConTextCap

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest

# Format code
black .
isort .
```

For detailed contributing guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

For development instructions, see [Developer Guide](docs/DEVELOPER_GUIDE.md).

## 📋 Roadmap

### 🎯 Version 1.1 (Next Release)
- [ ] Command-line interface (CLI)
- [ ] Custom exclusion patterns
- [ ] Batch processing support
- [ ] Configuration file support

### 🚀 Version 1.2 (Future)
- [ ] Export to Markdown and HTML
- [ ] Custom PDF templates
- [ ] Syntax highlighting in PDFs
- [ ] Dark mode for UI
- [ ] Multi-language support

### 🌟 Version 2.0 (Vision)
- [ ] CI/CD pipeline integration
- [ ] Plugin system
- [ ] Cloud storage integration
- [ ] Collaborative features
- [ ] Web-based version

Vote on features or suggest new ones in [Discussions](https://github.com/awaliuddin/ConTextCap/discussions)!

## 📊 Project Stats

<div align="center">

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/awaliuddin/ConTextCap)
![GitHub last commit](https://img.shields.io/github/last-commit/awaliuddin/ConTextCap)
![GitHub code size](https://img.shields.io/github/languages/code-size/awaliuddin/ConTextCap)
![Lines of code](https://img.shields.io/tokei/lines/github/awaliuddin/ConTextCap)

</div>

## 🙏 Acknowledgments

ConTextCap is built on the shoulders of giants:

- **[PyQt6](https://www.riverbankcomputing.com/software/pyqt/)**: Modern, powerful UI framework
- **[fpdf2](https://py-pdf.github.io/fpdf2/)**: Excellent Python PDF generation library
- **Open Source Community**: Icon styles and inspiration from amazing contributors

Special thanks to all our [contributors](https://github.com/awaliuddin/ConTextCap/graphs/contributors)!

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**TL;DR**: You can use, modify, and distribute this software freely. Just keep the original license and copyright notice.

## 🔗 Links

- **Documentation**: [User Guide](docs/USER_GUIDE.md) | [Developer Guide](docs/DEVELOPER_GUIDE.md)
- **Community**: [Discussions](https://github.com/awaliuddin/ConTextCap/discussions) | [Discord](#) (Coming Soon)
- **Support**: [Issues](https://github.com/awaliuddin/ConTextCap/issues) | [Security](SECURITY.md)
- **Social**: [Twitter](#) | [Blog](#) (Coming Soon)

## 💝 Support the Project

If you find ConTextCap useful, please consider:

- ⭐ **Starring** the repository
- 🐛 **Reporting bugs** via [Issues](https://github.com/awaliuddin/ConTextCap/issues)
- 💡 **Suggesting features** via [Feature Requests](https://github.com/awaliuddin/ConTextCap/issues/new?template=feature_request.md)
- 🔀 **Contributing** via [Pull Requests](https://github.com/awaliuddin/ConTextCap/pulls)
- 📢 **Sharing** with your network
- 💬 **Joining discussions** in our [community](https://github.com/awaliuddin/ConTextCap/discussions)

## 📞 Contact

- **Maintainer**: Asif Waliuddin
- **GitHub**: [@awaliuddin](https://github.com/awaliuddin)
- **Project**: [ConTextCap](https://github.com/awaliuddin/ConTextCap)

---

<div align="center">

**Made with ❤️ and ☕ by [Asif Waliuddin](https://github.com/awaliuddin) and the [Community](https://github.com/awaliuddin/ConTextCap/graphs/contributors)**

⭐ **Star us on GitHub — it motivates us a lot!** ⭐

[🏠 Homepage](https://github.com/awaliuddin/ConTextCap) • [📖 Docs](docs/) • [🐛 Report Bug](https://github.com/awaliuddin/ConTextCap/issues) • [✨ Request Feature](https://github.com/awaliuddin/ConTextCap/issues/new?template=feature_request.md)

</div>
