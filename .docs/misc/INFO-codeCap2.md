I'll help you integrate these additional features into the main codebase. Let me show you where and how to add them:

Now I'll explain the changes and additions:

1. **File Filtering (`is_allowed_file`)**
- Added at the top of the file with other utility functions
- Used to exclude common directories like `.git`, `__pycache__`, etc.
- Can be easily modified to add more exclusions or include specific file types

2. **File Icons (`get_file_icon`)**
- Added alongside `is_allowed_file`
- Maps mime types to appropriate icons
- Provides a default icon for unknown file types
- Note: You'll need to add actual icon files to an `icons` directory

3. **Settings Management**
- Added to `CodebaseCaptureWindow` class
- Uses `QSettings` for persistent storage
- Loads settings on startup
- Saves settings when closing the application

4. **UI Improvements**
- Replaced simple `QTextEdit` with `QTreeView` for better visualization
- Added status label for additional information
- Improved directory structure display with icons

To use these new features, you'll need to:

1. Create an `icons` directory in your project with icon files:
```
project_root/
  ├── icons/
  │   ├── text.png
  │   ├── python.png
  │   ├── js.png
  │   ├── html.png
  │   ├── css.png
  │   └── default.png
  ├── codebase_capture.py
  └── requirements.txt
```

2. Update the file scanning process to use the new filtering:
```python
for current_path in Path(self.root_path).rglob('*'):
    if is_allowed_file(current_path):
        # Process file...
```

3. Handle icon loading failures gracefully:
```python
def get_file_icon(file_path: Path) -> QIcon:
    try:
        mime_type, _ = mimetypes.guess_type(str(file_path))
        icon_path = f'icons/{mime_type.replace("/", "_")}.png'
        if os.path.exists(icon_path):
            return QIcon(icon_path)
    except Exception:
        pass
    return QIcon('icons/default.png')
```

Would you like me to add any other features or provide more detailed explanations of these changes?