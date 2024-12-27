#!/usr/bin/env python3

import sys
import os
from datetime import datetime
import mimetypes
from pathlib import Path
from typing import Optional

from PyQt6.QtCore import Qt, QThread, pyqtSignal, QSettings, QFileInfo
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QFileDialog, QProgressDialog,
    QMessageBox, QTreeView, QLabel, QComboBox, QStyle, QFileIconProvider
)
from fpdf import FPDF


class IconConfig:
    """Manages icon style configuration"""
    STYLES = ['classic', 'vivid', 'high-contrast', 'square-o']
    DEFAULT_STYLE = 'high-contrast'
    
    def __init__(self):
        self.current_style = self.DEFAULT_STYLE  # default style
        self.icon_root = Path('icons')  # path to icons directory
        
    def set_style(self, style: str):
        """Change the current icon style"""
        if style in self.STYLES:
            self.current_style = style
            return True
        return False
        
    def get_icon_path(self, icon_name: str) -> Path:
        """Get full path to icon file"""
        return self.icon_root / self.current_style / f"{icon_name}.svg"

class IconProvider:
    """Provides custom icons for files and folders"""
    def __init__(self):
        """Initialize the icon provider with custom icons"""
        self.config = IconConfig()
        self.icon_cache = {}
        
    def set_style(self, style: str):
        """Change icon style and clear cache"""
        if self.config.set_style(style):
            self.icon_cache.clear()  # Clear cache when style changes
            return True
        return False

    def get_icon(self, file_path: Path) -> QIcon:
        """Get icon for the given file path"""
        path_str = str(file_path)
        if path_str in self.icon_cache:
            return self.icon_cache[path_str]
                
        if file_path.is_dir():
            icon_path = self.config.get_icon_path('folder')
        else:
            extension = file_path.suffix.lower().lstrip('.')
            icon_path = self.config.get_icon_path(extension)
            if not icon_path.exists():
                icon_path = self.config.get_icon_path('file')
        
        icon = QIcon(str(icon_path))
        self.icon_cache[path_str] = icon
        return icon

def get_file_icon(file_path: Path) -> QIcon:
    """
    Return appropriate icon based on file type.

    This method checks if the icon provider is initialized, and if not, returns a default icon.
    """
    if ICON_PROVIDER is None:
        # Return a default icon if provider isn't initialized
        return QApplication.style().standardIcon(QStyle.StandardPixmap.SP_FileIcon)
    return ICON_PROVIDER.get_icon(file_path)

# Global icon provider instance (will be initialized in main)
ICON_PROVIDER = None

def initialize_icon_provider():
    """Initialize the global icon provider"""
    global ICON_PROVIDER
    ICON_PROVIDER = IconProvider()

def is_allowed_file(file_path: Path) -> bool:
    """
    Filter files based on extension or other criteria.
    
    Args:
        file_path: Path object to check
        
    Returns:
        bool: True if the file should be included, False otherwise
    """
    # Always allow directories
    if file_path.is_dir():
        return True
        
    # List of excluded patterns
    excluded = {'.git', '__pycache__', 'node_modules', '.idea', 'venv', '.pytest_cache', '.vscode'}
    
    # Check if any part of the path contains excluded patterns
    if any(ex in file_path.parts for ex in excluded):
        return False
        
    # Check if it's a hidden file (starts with .)
    if file_path.name.startswith('.'):
        return False
        
    return True

class DirectoryScanner(QThread):
    """
    Worker thread for scanning directories.

    This class emits signals for progress, structure ready, and error occurred.
    """
    progress = pyqtSignal(int)
    structure_ready = pyqtSignal(list)  # Changed from str to list
    error_occurred = pyqtSignal(str)
    
    def __init__(self, root_path: str):
        """
        Initialize the directory scanner.

        This method sets up the root path and initializes the total and processed items.
        """
        super().__init__()
        self.root_path = root_path
        self.total_items = 0
        self.processed_items = 0

    def run(self):
        """
        Run the directory scanner.

        This method scans the directory, generates the structure, and emits signals for progress and structure ready.
        """
        try:
            # First pass to count items for progress
            for _ in Path(self.root_path).rglob('*'):
                if is_allowed_file(_):
                    self.total_items += 1

            # Generate directory structure
            structure = []
            root = Path(self.root_path)
            
            # Process all files and directories
            for current_path in sorted(root.rglob('*')):
                try:
                    if not is_allowed_file(current_path):
                        continue
                        
                    # Get the relative path parts
                    rel_path = current_path.relative_to(root)
                    path_parts = list(rel_path.parts)
                    
                    # Create entry with full path info
                    entry = {
                        'name': current_path.name,
                        'path': str(current_path),
                        'is_file': current_path.is_file(),
                        'parts': path_parts
                    }
                    structure.append(entry)
                    
                    self.processed_items += 1
                    progress = int((self.processed_items / self.total_items) * 100)
                    self.progress.emit(progress)
                    
                except Exception as e:
                    self.error_occurred.emit(f"Error processing {current_path}: {str(e)}")
                    
            self.structure_ready.emit(structure)
            
        except Exception as e:
            self.error_occurred.emit(f"Error scanning directory: {str(e)}")

class PDFGenerator(QThread):
    """
    Worker thread for PDF generation.

    This class emits signals for progress, finished, and error occurred.
    """
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error_occurred = pyqtSignal(str)
    
    def __init__(self, root_path: str, output_path: str):
        """
        Initialize the PDF generator.

        This method sets up the root path, output path, and initializes the total and processed files.
        """
        super().__init__()
        self.root_path = root_path
        self.output_path = output_path
        self.total_files = 0
        self.processed_files = 0
        
    def generate_tree_structure(self):
        """Generate a clean tree structure for PDF."""
        structure = []
        root = Path(self.root_path)
        
        def add_to_structure(path, depth=0):
            if not path.is_file() and not path.is_dir():
                return
            
            try:
                prefix = "    " * depth + ("└── " if depth > 0 else "")
                structure.append(prefix + path.name)
                
                if path.is_dir():
                    for child in sorted(path.iterdir()):
                        if is_allowed_file(child):
                            add_to_structure(child, depth + 1)
            except Exception as e:
                print(f"Error processing {path}: {e}")
        
        add_to_structure(root)
        return structure

    def run(self):
        """Run the PDF generator."""
        try:
            # Count total files first
            self.total_files = 0
            for _ in Path(self.root_path).rglob('*'):
                if _.is_file() and is_allowed_file(_):
                    self.total_files += 1

            # Create PDF
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            
            # Add first page
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            title = f"Codebase Capture: {Path(self.root_path).name}"
            pdf.cell(0, 10, title, ln=True, align='C')
            
            # Add timestamp
            pdf.set_font('Arial', '', 10)
            timestamp = f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            pdf.cell(0, 10, timestamp, ln=True, align='C')
            
            # Add directory structure
            pdf.add_page()
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 10, "Directory Structure:", ln=True)
            pdf.set_font('Arial', '', 10)
            
            # Generate and add tree structure
            tree_structure = self.generate_tree_structure()
            for line in tree_structure:
                # Clean the line text
                line_text = str(line).encode('ascii', errors='replace').decode('ascii')
                pdf.cell(0, 5, line_text, ln=True)
            
            # Process each file
            for file_path in Path(self.root_path).rglob('*'):
                if file_path.is_file() and is_allowed_file(file_path):
                    try:
                        # Check if file is text-based
                        mime_type, _ = mimetypes.guess_type(str(file_path))
                        if mime_type and ('text' in mime_type or 'application/json' in mime_type):
                            # Add file header
                            pdf.add_page()
                            pdf.set_font('Arial', 'B', 12)
                            rel_path = str(file_path.relative_to(self.root_path))
                            pdf.cell(0, 10, f"File: {rel_path}", ln=True)
                            
                            # Add file content
                            pdf.set_font('Arial', '', 8)
                            try:
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    # Split content into lines and clean them
                                    for line in content.split('\n'):
                                        # Replace non-ASCII characters
                                        line_text = str(line).encode('ascii', errors='replace').decode('ascii')
                                        pdf.multi_cell(0, 5, line_text)
                            except UnicodeDecodeError:
                                pdf.multi_cell(0, 5, "[Binary file contents not shown]")
                            except Exception as e:
                                pdf.multi_cell(0, 5, f"[Error reading file: {str(e)}]")
                            
                        self.processed_files += 1
                        progress = int((self.processed_files / self.total_files) * 100)
                        self.progress.emit(progress)
                        
                    except Exception as e:
                        self.error_occurred.emit(f"Error processing file {file_path}: {str(e)}")
                        continue

            # Save the PDF
            pdf.output(self.output_path)
            self.finished.emit()
            
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            self.error_occurred.emit(f"Error generating PDF: {str(e)}\n{error_details}")

class CodebaseCaptureWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the codebase capture window.

        This method sets up the window title, geometry, and initializes the selected path and exclude patterns.
        """
        super().__init__()
        self.selected_path: Optional[str] = None
        self.exclude_patterns = set()  # For file filtering
        self.initUI()  # Create UI elements first
        self.load_settings()  # Then load settings

    def initUI(self):
        """
        Initialize the user interface.

        This method sets up the central widget, layout, buttons, tree view, and status label.
        """
        self.setWindowTitle('Codebase Capture')
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create buttons
        set_location_btn = QPushButton('Set Codebase Location')
        create_pdf_btn = QPushButton('Create PDF')
        
        # Add style selector
        style_layout = QHBoxLayout()
        style_label = QLabel("Icon Style:")
        self.style_combo = QComboBox()
        self.style_combo.addItems(IconConfig.STYLES)
        style_layout.addWidget(style_label)
        style_layout.addWidget(self.style_combo)
        style_layout.addStretch()
        
        # Create tree view for directory structure
        self.tree_view = QTreeView()
        self.tree_model = QStandardItemModel()
        self.tree_model.setHorizontalHeaderLabels(['File Structure'])
        self.tree_view.setModel(self.tree_model)
        
        # Create status label
        self.status_label = QLabel()
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        # Add widgets to layout
        layout.addWidget(set_location_btn)
        layout.addWidget(create_pdf_btn)
        layout.addLayout(style_layout)
        layout.addWidget(self.tree_view)
        layout.addWidget(self.status_label)

        # Connect signals
        set_location_btn.clicked.connect(self.select_directory)
        create_pdf_btn.clicked.connect(self.create_pdf)
        self.style_combo.currentTextChanged.connect(self.on_style_changed)
        
    def on_style_changed(self, style: str):
        """Handle icon style changes"""
        if ICON_PROVIDER.set_style(style):
            # Save the style preference
            settings = QSettings('CodebaseCapture', 'Settings')
            settings.setValue('icon_style', style)
            # Refresh the tree view with new icons
            if self.selected_path:
                self.refresh_tree_view()
                
    def refresh_tree_view(self):
        """Refresh the tree view to update icons"""
        if self.selected_path:
            self.scanner = DirectoryScanner(self.selected_path)
            self.scanner.structure_ready.connect(self.display_structure)
            self.scanner.error_occurred.connect(self.show_error)
            self.scanner.start()
            
    def select_directory(self):
        """
        Handle directory selection.

        This method opens a file dialog for selecting a directory and creates a progress dialog.
        """
        directory = QFileDialog.getExistingDirectory(self, "Select Codebase Directory")
        if directory:
            self.selected_path = directory
            
            # Create and configure progress dialog
            progress = QProgressDialog("Scanning directory...", "Cancel", 0, 100, self)
            progress.setWindowModality(Qt.WindowModality.WindowModal)
            progress.show()

            # Create and start scanner thread
            self.scanner = DirectoryScanner(directory)
            self.scanner.progress.connect(progress.setValue)
            self.scanner.structure_ready.connect(self.display_structure)
            self.scanner.error_occurred.connect(self.show_error)
            self.scanner.start()

    def create_pdf(self):
        """
        Handle PDF creation.

        This method checks if a directory is selected, opens a file dialog for saving the PDF, and creates a progress dialog.
        """
        if not self.selected_path:
            QMessageBox.warning(self, "Error", "Please select a codebase directory first.")
            return

        output_path, _ = QFileDialog.getSaveFileName(
            self, "Save PDF", "", "PDF Files (*.pdf)"
        )
        
        if output_path:
            # Create and configure progress dialog
            progress = QProgressDialog("Generating PDF...", "Cancel", 0, 100, self)
            progress.setWindowModality(Qt.WindowModality.WindowModal)
            progress.show()

            # Create and start PDF generator thread
            self.pdf_generator = PDFGenerator(self.selected_path, output_path)
            self.pdf_generator.progress.connect(progress.setValue)
            self.pdf_generator.finished.connect(
                lambda: QMessageBox.information(self, "Success", "PDF generated successfully!")
            )
            self.pdf_generator.error_occurred.connect(self.show_error)
            self.pdf_generator.start()

    def display_structure(self, structure: list):
        """Display the directory structure in tree view."""
        self.tree_model.clear()
        self.tree_model.setHorizontalHeaderLabels(['File Structure'])
        
        # Create root item
        root_path = Path(self.selected_path)
        root_item = QStandardItem(get_file_icon(root_path), root_path.name)
        self.tree_model.appendRow(root_item)
        
        # Keep track of items by their path parts
        items = {(): root_item}
        
        # Sort entries to ensure parents come before children
        for entry in sorted(structure, key=lambda x: len(x['parts'])):
            try:
                # Get parent path parts
                parent_parts = tuple(entry['parts'][:-1])
                parent_item = items.get(parent_parts, root_item)
                
                # Create item with appropriate icon
                path = Path(entry['path'])
                item = QStandardItem(get_file_icon(path), entry['name'])
                
                # Add item to parent
                parent_item.appendRow(item)
                
                # Store item reference if it might have children
                if not entry['is_file']:
                    items[tuple(entry['parts'])] = item
                    
            except Exception as e:
                self.show_error(f"Error adding item {entry['name']}: {str(e)}")
        
        self.tree_view.expandAll()
        
    def load_settings(self):
        """
        Load application settings.

        This method loads the last directory, exclude patterns, and icon style from the settings.
        """
        settings = QSettings('CodebaseCapture', 'Settings')
        self.selected_path = settings.value('last_directory', None)
        self.exclude_patterns = set(settings.value('exclude_patterns', []))
        
        # Load and apply icon style
        style = settings.value('icon_style', IconConfig.DEFAULT_STYLE)
        if ICON_PROVIDER and style in IconConfig.STYLES:
            ICON_PROVIDER.set_style(style)
            self.style_combo.setCurrentText(style)
        
    def save_settings(self):
        """
        Save application settings.

        This method saves the last directory, exclude patterns, and icon style to the settings.
        """
        settings = QSettings('CodebaseCapture', 'Settings')
        if self.selected_path:
            settings.setValue('last_directory', self.selected_path)
        
        # Convert exclude patterns set to list for storage
        settings.setValue('exclude_patterns', list(self.exclude_patterns))
        
    def closeEvent(self, event):
        """
        Save settings when closing the application.

        This method saves the settings and calls the close event of the parent class.
        """
        self.save_settings()
        super().closeEvent(event)

    def show_error(self, message: str):
        """
        Display error message.

        This method shows a critical message box with the error message.
        """
        QMessageBox.critical(self, "Error", message)

def main():
    # Initialize application
    app = QApplication(sys.argv)
    
    # Initialize icon provider after QApplication is created
    initialize_icon_provider()
    
    # Create and show main window
    window = CodebaseCaptureWindow()
    window.show()
    
    # Start event loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()