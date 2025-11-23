# Frequently Asked Questions (FAQ)

## General Questions

### What is ConTextCap?

ConTextCap (Context Capture) is a desktop application that transforms your entire codebase into a single, comprehensive PDF document. It's perfect for sharing with LLMs, code reviews, documentation, and archiving.

### Why would I need this?

- **LLM Integration**: Feed your complete codebase to ChatGPT, Claude, or other AI assistants
- **Code Reviews**: Share entire project context with reviewers
- **Documentation**: Create point-in-time snapshots of your projects
- **Onboarding**: Help new team members understand the codebase
- **Archiving**: Preserve legacy projects in a portable format

### Is ConTextCap free?

Yes! ConTextCap is open-source software licensed under the MIT License. You can use, modify, and distribute it freely.

## Installation & Setup

### What are the system requirements?

- **Python**: 3.8 or higher
- **OS**: Windows, macOS, or Linux
- **RAM**: 512MB minimum (2GB+ recommended for large projects)
- **Disk Space**: 100MB for installation + space for output PDFs

### How do I install ConTextCap?

```bash
# Via pip (recommended)
pip install contextcap

# From source
git clone https://github.com/awaliuddin/ConTextCap.git
cd ConTextCap
pip install -r requirements.txt
```

### Installation failed. What should I do?

1. Ensure Python 3.8+ is installed: `python --version`
2. Update pip: `pip install --upgrade pip`
3. Install dependencies separately:
   ```bash
   pip install PyQt6
   pip install fpdf2
   ```
4. Check our [Troubleshooting Guide](USER_GUIDE.md#troubleshooting)

## Usage Questions

### How do I generate a PDF?

1. Launch ConTextCap: `python ConTextCap.py`
2. Click "Select Directory" and choose your project
3. Select an icon style (optional)
4. Click "Generate PDF"
5. Choose where to save the output

### Can I use ConTextCap from the command line?

Command-line interface is planned for v1.1. Currently, use the GUI application.

### What file types are supported?

**Text Files** (full content included):
- Code: `.py`, `.js`, `.ts`, `.java`, `.cpp`, `.go`, `.rs`, etc.
- Web: `.html`, `.css`, `.jsx`, `.tsx`, `.vue`
- Data: `.json`, `.xml`, `.yaml`, `.toml`
- Docs: `.md`, `.rst`, `.txt`

**Binary Files** (metadata only):
- Images, PDFs, archives, executables, etc.

### How do I exclude certain files or directories?

ConTextCap automatically excludes common directories like `.git`, `node_modules`, `__pycache__`, etc. Custom exclusions will be available in v1.1 via configuration files.

### Can I customize the PDF output?

Currently, the PDF layout is standardized. Custom templates and styling options are planned for v1.2.

## Performance Questions

### How long does it take to generate a PDF?

- **Small projects** (<100 files): Seconds
- **Medium projects** (100-1000 files): 1-5 minutes
- **Large projects** (1000+ files): 5-15 minutes

Performance depends on file count, sizes, and system specs.

### My project has 10,000 files. Will it work?

Yes, but it may take a while. Consider:
- Excluding test directories
- Processing only source code directories
- Using a faster machine with SSD storage

### How can I speed up PDF generation?

1. Exclude unnecessary directories
2. Process specific subdirectories only
3. Use an SSD for faster I/O
4. Close other applications to free up RAM

### What's the maximum project size?

There's no hard limit, but practical limits exist:
- **Files**: 10,000+ files work but take time
- **File size**: Individual files >10MB may slow processing
- **PDF size**: PDFs >100MB may be slow to open

## LLM Integration

### Which LLMs can I use this with?

ConTextCap works with any LLM that accepts PDF uploads:
- ChatGPT (Plus/Pro with PDF support)
- Claude (via Anthropic Console)
- Google Gemini
- Microsoft Copilot
- Local LLMs (LM Studio, Ollama, etc.)

### How do I upload to ChatGPT?

1. Generate your PDF with ConTextCap
2. Open ChatGPT
3. Click the attachment icon
4. Upload your PDF
5. Ask questions about your codebase

### The PDF is too large for my LLM. What can I do?

1. Process only relevant directories
2. Exclude test files and documentation
3. Split large projects into smaller sections
4. Use compression (though this is automatic)

### Can LLMs actually understand the PDF format?

Yes! Modern LLMs can parse and understand PDF content, including code structure, file organization, and documentation.

## Technical Questions

### Does ConTextCap work offline?

Yes! ConTextCap is 100% offline. No internet connection is required, and your code never leaves your machine.

### Is my code secure?

Absolutely! ConTextCap:
- Runs entirely on your local machine
- Never uploads or transmits code
- Doesn't phone home
- Doesn't collect telemetry

### Can I run ConTextCap in Docker?

Yes! See our [Docker Guide](DOCKER.md) for details.

```bash
docker run -v $(pwd)/project:/data/project:ro \
           -v $(pwd)/output:/data/output \
           contextcap:latest
```

### Can I integrate ConTextCap into CI/CD?

Yes! Example GitHub Actions workflow:

```yaml
- name: Generate Documentation PDF
  run: |
    pip install contextcap
    contextcap --input ./src --output ./docs.pdf
```

## Output & Format Questions

### What format is the output?

ConTextCap generates standard PDF documents (PDF 1.4+), compatible with all PDF readers.

### Can I export to other formats?

Currently, only PDF is supported. Markdown and HTML export are planned for v1.2.

### Can I edit the generated PDF?

Yes, the PDF can be opened in any PDF editor (Adobe Acrobat, PDF-XChange, etc.). However, it's generated programmatically, so manual editing may be tedious.

### Can I add my own branding/logo?

Custom branding and templates are planned for v1.2.

## Troubleshooting

### "Qt platform plugin error" when running

**Solution**: Install required system libraries

```bash
# Ubuntu/Debian
sudo apt-get install libegl1 libxkbcommon-x11-0

# macOS
# Usually works out of box with PyQt6

# Windows
# Usually works out of box with PyQt6
```

### PDF generation fails with "Permission denied"

**Causes**:
- Output directory is read-only
- File is open in a PDF reader
- Insufficient disk space

**Solutions**:
- Choose a different output location
- Close the PDF if it's open
- Free up disk space

### Special characters appear incorrectly

**Solution**: This is usually an encoding issue
- Ensure source files are UTF-8 encoded
- Update to the latest version of ConTextCap
- Report the issue on GitHub with a sample file

### The generated PDF is very large

**Why**: PDFs include full text content of all files

**Solutions**:
- Exclude unnecessary files
- Process smaller directory sets
- Use PDF compression tools

### ConTextCap crashed while processing

**Steps**:
1. Note which file it was processing
2. Check if that file is corrupted
3. Try excluding that file/directory
4. Report the bug on GitHub with details

## Feature Requests

### Can you add feature X?

Maybe! Check our [Roadmap](../README.md#roadmap) or open a [feature request](https://github.com/awaliuddin/ConTextCap/issues/new?template=feature_request.md).

### When will CLI support be added?

CLI is planned for v1.1 (next release).

### Will there be a web version?

A web-based version is in our v2.0 vision, but it's a long-term goal.

### Can I contribute?

Yes! We love contributions. See our [Contributing Guide](../CONTRIBUTING.md).

## Community & Support

### Where can I get help?

- **Documentation**: [User Guide](USER_GUIDE.md)
- **Issues**: [GitHub Issues](https://github.com/awaliuddin/ConTextCap/issues)
- **Discussions**: [GitHub Discussions](https://github.com/awaliuddin/ConTextCap/discussions)

### How do I report a bug?

Open a [bug report](https://github.com/awaliuddin/ConTextCap/issues/new?template=bug_report.md) with:
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version)
- Error messages or logs

### How can I contribute?

- Report bugs
- Suggest features
- Improve documentation
- Submit code via pull requests
- Help other users in Discussions

### Is there a community forum?

Use [GitHub Discussions](https://github.com/awaliuddin/ConTextCap/discussions) for:
- Questions
- Ideas
- Show and tell
- General discussion

## Licensing & Legal

### What license is ConTextCap under?

MIT License - you can use, modify, and distribute freely with attribution.

### Can I use this for commercial projects?

Yes! The MIT License allows commercial use.

### Do I need to credit ConTextCap?

Attribution is appreciated but not required by the MIT License.

### Can I sell ConTextCap or PDF generated by it?

You can sell services using ConTextCap, but you cannot sell ConTextCap itself as your own product (must maintain attribution).

---

**Still have questions?** Ask in [GitHub Discussions](https://github.com/awaliuddin/ConTextCap/discussions)!
