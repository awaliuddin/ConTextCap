# Codebase Capture - Setup Instructions

## Dependencies
The application requires Python 3.8+ and the following packages:
- PyQt6
- fpdf
- mimetypes (part of Python standard library)

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install required packages:
```bash
pip install PyQt6 fpdf
```

3. Run the application:
```bash
python codebase_capture.py
```

## Usage

1. Launch the application
2. Click "Set Codebase Location" to select your project directory
3. Review the displayed directory structure
4. Click "Create PDF" to generate a PDF document of your codebase
5. Select the save location for your PDF

## Notes

- The application supports text-based files (code, configuration, documentation)
- Binary files are noted but their contents are not included in the PDF
- Large codebases may take some time to process
- Progress indicators show status during scanning and PDF generation

## Troubleshooting

If you encounter any errors:
- Ensure you have write permissions in the output directory
- Check that the selected directory is accessible
- For large codebases, allow sufficient time for processing
- If PDF generation fails, try with a smaller subset of files first