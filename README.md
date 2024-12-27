# ConTextCap 📚

A powerful desktop application that captures and documents your codebase by generating beautiful PDF documentation of your project's structure and contents.

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

1. Clone the repository:
```bash
git clone https://github.com/awaliuddin/ConTextCap.git
cd ConTextCap
```

2. Install the required dependencies:
```bash
pip install PyQt6 fpdf
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

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Built with PyQt6 for the modern UI
- Uses FPDF for PDF generation
- Icon styles provided by various open-source contributors

---

Made with ❤️ by Asif Waliuddin
