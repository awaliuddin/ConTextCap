# ConTextCap 📚
[![GitHub license](https://img.shields.io/github/license/awaliuddin/ConTextCap)](https://github.com/awaliuddin/ConTextCap/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/awaliuddin/ConTextCap)](https://github.com/awaliuddin/ConTextCap/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/awaliuddin/ConTextCap)](https://github.com/awaliuddin/ConTextCap/issues)
[![GitHub forks](https://img.shields.io/github/forks/awaliuddin/ConTextCap)](https://github.com/awaliuddin/ConTextCap/network)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)

> 🚀 ConTextCap = "Context Capture" A powerful desktop application that captures and documents your project codebase and artifacts by generating a single, beautiful PDF document to feed to your LLM of choice. 🥳

[Demo Screenshot/GIF Coming Soon]

## Features ✨

- 🌳 **Directory Tree Visualization**: Displays your project's structure in an easy-to-read tree format
- 📄 **Code Content Capture**: Includes the full content of text-based files (code, markdown, config files, etc.)
- 📊 **Binary File Information**: Shows size and type information for non-text files
- 🎨 **Customizable Icon Styles**: Choose from multiple icon styles for file and folder representation
- 🔍 **Smart File Filtering**: Automatically excludes common non-essential directories (like `.git`, `__pycache__`, etc.)
- 📱 **Modern UI**: Built with PyQt6 for a clean and intuitive user experience

## Requirements 🛠️

- Python 3.6+
- PyQt6
- FPDF

## Installation 📦

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Quick Start
1. Clone the repository:
```bash
git clone https://github.com/awaliuddin/ConTextCap.git
cd ConTextCap
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage 🚀

1. Run the application:
```bash
python ConTextCap.py
```

2. Use the interface to:
   - Select a directory to document
   - Choose your preferred icon style
   - Generate a PDF documentation

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

## Contributing 🤝

We love your input! We want to make contributing to ConTextCap as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

### Development Process

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

### Any contributions you make will be under the MIT Software License
In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Roadmap 🗺️

- [ ] Add support for more file types
- [ ] Custom theming options
- [ ] Export in multiple formats (MD, HTML)
- [ ] Batch processing capabilities
- [ ] Integration with CI/CD pipelines

## Support 💝

If you found this project interesting or helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting [bugs/issues](https://github.com/awaliuddin/ConTextCap/issues)
- 💡 Suggesting new features
- 🔀 Creating pull requests

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Built with PyQt6 for the modern UI
- Uses FPDF for PDF generation
- Icon styles provided by various open-source contributors

---

Made with ❤️ by Asif Waliuddin
