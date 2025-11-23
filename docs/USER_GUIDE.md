# ConTextCap User Guide

Welcome to ConTextCap! This guide will help you get the most out of the application.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Features](#features)
5. [Advanced Usage](#advanced-usage)
6. [Tips and Tricks](#tips-and-tricks)
7. [Troubleshooting](#troubleshooting)
8. [FAQ](#faq)

## Introduction

ConTextCap (Context Capture) is a powerful desktop application that captures and documents your project codebase by generating a single, comprehensive PDF document. This makes it easy to:

- Share your codebase with LLMs (Large Language Models)
- Review project structure and contents
- Create documentation snapshots
- Archive project states
- Onboard new team members

## Installation

### Method 1: Install via pip (Recommended)

```bash
pip install contextcap
```

### Method 2: Install from Source

```bash
# Clone the repository
git clone https://github.com/awaliuddin/ConTextCap.git
cd ConTextCap

# Install dependencies
pip install -r requirements.txt

# Run the application
python ConTextCap.py
```

### System Requirements

- **Python**: 3.8 or higher
- **Operating Systems**: Windows, macOS, Linux
- **Dependencies**: PyQt6, fpdf2

## Getting Started

### Quick Start

1. **Launch ConTextCap**
   ```bash
   # If installed via pip
   contextcap

   # If running from source
   python ConTextCap.py
   ```

2. **Select a Directory**
   - Click the "Select Directory" button
   - Navigate to your project folder
   - Click "Select Folder"

3. **Choose Icon Style** (Optional)
   - Select from available icon styles:
     - Classic
     - Vivid
     - High Contrast
     - Square-O

4. **Generate PDF**
   - Click "Generate PDF"
   - Choose where to save the output
   - Wait for the process to complete

### First Project

Let's create a PDF of a sample project:

1. Create a test directory with some files:
   ```bash
   mkdir my-test-project
   cd my-test-project
   echo "# My Project" > README.md
   echo "print('Hello World')" > main.py
   ```

2. Launch ConTextCap and select the `my-test-project` directory

3. Generate the PDF and review the output

## Features

### Directory Tree Visualization

ConTextCap displays your project structure in a hierarchical tree format, making it easy to understand your project's organization.

**Features:**
- Nested directory structure
- File and folder icons
- File size information
- Clear visual hierarchy

### Code Content Capture

All text-based files are included with their full content:

**Supported File Types:**
- Python (`.py`)
- JavaScript (`.js`)
- JSON (`.json`)
- XML (`.xml`)
- Markdown (`.md`)
- Text files (`.txt`)
- reStructuredText (`.rst`)
- Log files (`.log`)
- Configuration files (`.ini`, `.conf`, `.cfg`)

### Binary File Information

For binary files, ConTextCap includes:
- File name and path
- File size
- File type/MIME type

### Smart File Filtering

ConTextCap automatically excludes common non-essential directories:

**Excluded Directories:**
- `.git` - Git version control
- `__pycache__` - Python cache
- `node_modules` - Node.js dependencies
- `.venv`, `venv`, `env` - Virtual environments
- `.idea` - IDE settings
- `dist`, `build` - Build outputs

### Customizable Icon Styles

Choose from multiple icon styles to match your preference:

1. **Classic**: Traditional file/folder icons
2. **Vivid**: Colorful, modern icons
3. **High Contrast**: Easy-to-read, accessible icons
4. **Square-O**: Minimalist square icons

### Progress Tracking

For large projects, ConTextCap shows:
- Current file being processed
- Overall progress percentage
- Estimated time remaining

## Advanced Usage

### Command Line Options

ConTextCap can be run with command-line arguments (feature to be implemented):

```bash
# Specify input directory
contextcap --input /path/to/project

# Specify output file
contextcap --output /path/to/output.pdf

# Choose icon style
contextcap --style vivid

# Exclude additional patterns
contextcap --exclude "*.log,*.tmp"
```

### Customizing Exclusions

To customize which files and directories are excluded, you can modify the exclusion list in the settings (feature to be implemented).

### Batch Processing

Process multiple projects at once (feature to be implemented):

```bash
contextcap --batch projects.txt
```

## Tips and Tricks

### 1. Optimize for LLM Input

When preparing code for LLMs:
- Focus on source code directories
- Exclude large binary files
- Include README and documentation files
- Remove test data if not needed

### 2. Create Project Snapshots

Use ConTextCap to create regular project snapshots:
- Before major refactoring
- At release milestones
- For code reviews
- When switching contexts

### 3. Documentation Archives

Create documentation archives that include:
- Source code
- README files
- Configuration files
- API documentation

### 4. Share with Team

Generate PDFs to:
- Share project overview with stakeholders
- Help new developers understand the codebase
- Create portable code reviews
- Archive legacy projects

## Troubleshooting

### PDF Generation Fails

**Problem**: PDF generation stops with an error

**Solutions**:
- Check that you have write permissions to the output directory
- Ensure the output path is valid
- Try a different output location
- Check for special characters in file names

### Large Projects Take Too Long

**Problem**: PDF generation is very slow for large projects

**Solutions**:
- Exclude unnecessary directories (node_modules, etc.)
- Process only specific subdirectories
- Use a faster storage drive (SSD)

### Unicode/Encoding Errors

**Problem**: Special characters appear incorrectly

**Solutions**:
- Ensure files are UTF-8 encoded
- Update to the latest version of ConTextCap
- Report the issue on GitHub with a sample file

### Missing Icons

**Problem**: Icons don't appear in the PDF

**Solutions**:
- Verify the icons directory exists
- Check that icon files are present
- Reinstall ConTextCap
- Try a different icon style

## FAQ

### Q: What's the maximum project size ConTextCap can handle?

A: ConTextCap can handle projects with thousands of files. However, very large projects (>10,000 files) may take several minutes to process.

### Q: Can I customize the PDF layout?

A: Currently, the PDF layout is fixed. Custom layouts are planned for a future release.

### Q: Does ConTextCap work offline?

A: Yes! ConTextCap works entirely offline. No internet connection is required.

### Q: Can I use ConTextCap in my CI/CD pipeline?

A: Yes! ConTextCap can be integrated into CI/CD pipelines for automated documentation generation.

### Q: Is there a file size limit for the generated PDF?

A: No hard limit, but PDFs larger than 100MB may be slow to open in some PDF readers.

### Q: Can I contribute to ConTextCap?

A: Absolutely! Check out our [Contributing Guide](../CONTRIBUTING.md) to get started.

### Q: How do I report bugs or request features?

A: Please open an issue on our [GitHub Issues](https://github.com/awaliuddin/ConTextCap/issues) page.

## Getting Help

If you need additional help:

- 📖 Read the [Documentation](https://github.com/awaliuddin/ConTextCap#readme)
- 🐛 Report [Issues](https://github.com/awaliuddin/ConTextCap/issues)
- 💬 Join [Discussions](https://github.com/awaliuddin/ConTextCap/discussions)
- ⭐ Star the [Repository](https://github.com/awaliuddin/ConTextCap)

---

Thank you for using ConTextCap! 🚀
