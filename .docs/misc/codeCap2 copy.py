#!/usr/bin/env python3

import sys
import os
from pathlib import Path
from typing import Optional
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QPushButton, QTextEdit, QFileDialog, QProgressDialog,
    QMessageBox, QTreeView, QLabel, QStyle, QFileIconProvider
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QSettings, QFileInfo
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
import fpdf
import mimetypes

class IconProvider:
    """Provides system icons for files and folders"""
    def __init__(self):
        """
        Initialize the icon provider.

        This method sets up the style and cache for icons.
        """
        self.style = QApplication.style()
        # Cache for frequently used icons
        self.icon_cache = {}
        
        # Initialize standard icons
        self.folder_icon = self.style.standardIcon(QStyle.StandardPixmap.SP_DirIcon)
        self.file_icon = self.style.standardIcon(QStyle.StandardPixmap.SP_FileIcon)

    def get_icon(self, file_path: Path) -> QIcon:
        """
        Get system icon for the given file path.

        This method checks the cache first, then determines the icon based on the file path.
        If the file is a directory, it assigns the folder icon. Otherwise, it determines the file type based on extension.
        """
        path_str = str(file_path)
        if path_str in self.icon_cache:
            return self.icon_cache[path_str]
                
        file_info = QFileInfo(path_str)
        
        if file_info.isDir():
            icon = self.folder_icon
        else:
            extension = file_info.suffix().lower()
            icon = self.get_icon_by_extension(extension)

        self.icon_cache[path_str] = icon
        return icon
        
    def get_icon_by_extension(self, extension: str) -> QIcon:
        if extension in ['py', 'pyw']:
            return self.style.standardIcon(QStyle.StandardPixmap.SP_CommandLink)
        elif extension in ['html', 'htm']:
            return self.style.standardIcon(QStyle.StandardPixmap.SP_DriveCDIcon)
        elif extension == 'pdf':
            return self.style.standardIcon(QStyle.StandardPixmap.SP_DirLinkIcon)
        elif extension in ['jpg', 'jpeg', 'png', 'gif']:
            return self.style.standardIcon(QStyle.StandardPixmap.SP_DirIcon)
        elif extension in ['doc', 'docx']:
            return self.style.standardIcon(QStyle.StandardPixmap.SP_FileIcon)
        elif extension in ['xls', 'xlsx']:
            return self.style.standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)
        elif extension in ['ppt', 'pptx']:
            return self.style.standardIcon(QStyle.StandardPixmap.SP_TrashIcon)
        elif extension in ['mp3', 'wav']:
            return self.style.standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
        elif extension in ['mp4', 'avi', 'mov']:
            return self.style.standardIcon(QStyle.StandardPixmap.SP_MediaStop)
        else:
            return self.file_icon

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

    This method checks if the file path contains any excluded patterns.
    """
    excluded = {'.git', '__pycache__', 'node_modules', '.idea', 'venv'}
    return not any(ex in file_path.parts for ex in excluded)

class DirectoryScanner(QThread):
    """
    Worker thread for scanning directories.

    This class emits signals for progress, structure ready, and error occurred.
    """
    progress = pyqtSignal(int)
    structure_ready = pyqtSignal(str)
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
            for current_path in Path(self.root_path).rglob('*'):
                try:
                    if not is_allowed_file(current_path):
                        continue
                        
                    rel_path = current_path.relative_to(self.root_path)
                    depth = len(rel_path.parts) - 1
                    prefix = '│   ' * depth + '├── ' if depth > 0 else ''
                    structure.append(f"{prefix}{current_path.name}")
                    
                    self.processed_items += 1
                    progress = int((self.processed_items / self.total_items) * 100)
                    self.progress.emit(progress)
                    
                except Exception as e:
                    self.error_occurred.emit(f"Error processing {current_path}: {str(e)}")
                    
            self.structure_ready.emit('\n'.join(structure))
            
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

    def run(self):
        """
        Run the PDF generator.

        This method generates the PDF, adds title and timestamp, and processes each file.
        """
        try:
            # Count total files first
            for _ in Path(self.root_path).rglob('*'):
                if _.is_file() and is_allowed_file(_):
                    self.total_files += 1

            # Create PDF
            pdf = fpdf.FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            
            # Add title
            pdf.set_font("Arial", "B", 16)
            title = f"Codebase Capture: {Path(self.root_path).name}"
            pdf.cell(0, 10, title, ln=True, align='C')
            
            # Add timestamp
            pdf.set_font("Arial", "I", 10)
            timestamp = f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            pdf.cell(0, 10, timestamp, ln=True, align='C')
            
            # Process each file
            for file_path in Path(self.root_path).rglob('*'):
                if file_path.is_file() and is_allowed_file(file_path):
                    try:
                        # Check if file is text-based
                        mime_type, _ = mimetypes.guess_type(str(file_path))
                        if mime_type and ('text' in mime_type or 'application/json' in mime_type):
                            # Add file header
                            pdf.add_page()
                            pdf.set_font("Arial", "B", 12)
                            rel_path = file_path.relative_to(self.root_path)
                            pdf.cell(0, 10, f"File: {rel_path}", ln=True)
                            

                            # Add file content
                            pdf.set_font("Courier", size=8)
                            try:
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    # Split content into lines and add to PDF
                                    for line in content.split('\n'):
                                        pdf.multi_cell(0, 5, line)
                            except UnicodeDecodeError:
                                pdf.multi_cell(0, 5, "[Binary file contents not shown]")
                                

                        self.processed_files += 1
                        progress = int((self.processed_files / self.total_files) * 100)
                        self.progress.emit(progress)
                        
                    except Exception as e:
                        self.error_occurred.emit(f"Error processing {file_path}: {str(e)}")
                        continue

            # Save PDF
            pdf.output(self.output_path)
            self.finished.emit()
            
        except Exception as e:
            self.error_occurred.emit(f"Error generating PDF: {str(e)}")

class CodebaseCaptureWindow(QMainWindow):
    def __init__(self):
        """
        Initialize the codebase capture window.

        This method sets up the window title, geometry, and initializes the selected path and exclude patterns.
        """
        super().__init__()
        self.selected_path: Optional[str] = None
        self.exclude_patterns = set()  # For file filtering
        self.load_settings()
        self.initUI()

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
        layout.addWidget(self.tree_view)
        layout.addWidget(self.status_label)

        # Connect signals
        set_location_btn.clicked.connect(self.select_directory)
        create_pdf_btn.clicked.connect(self.create_pdf)

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

    def display_structure(self, structure: str):
        """
        Display the directory structure in tree view.

        This method clears the tree model, sets the header labels, and adds items to the tree view.
        """
        self.tree_model.clear()
        self.tree_model.setHorizontalHeaderLabels(['File Structure'])
        
        root_item = QStandardItem(get_file_icon(Path(self.selected_path)), Path(self.selected_path).name)
        self.tree_model.appendRow(root_item)
        
        current_items = {0: root_item}
        
        for line in structure.split('\n'):
            if not line.strip():
                continue
                
            # Calculate depth based on the number of directory separators
            parts = line.split('├── ')[-1].split('/')
            depth = len(parts) - 1
            name = parts[-1]
            
            # Create item with appropriate icon
            path = Path(self.selected_path) / '/'.join(parts)
            item = QStandardItem(get_file_icon(path), name)
            
            # Find the correct parent item
            parent_depth = depth - 1
            parent_item = current_items.get(parent_depth, root_item)
            
            # Add item to appropriate parent
            parent_item.appendRow(item)
            current_items[depth] = item
        
        self.tree_view.expandAll()
        
    def load_settings(self):
        """
        Load application settings.

        This method loads the last directory and exclude patterns from the settings.
        """
        settings = QSettings('CodebaseCapture', 'Settings')
        self.selected_path = settings.value('last_directory', None)
        
        # Load exclude patterns as a list and convert to set
        exclude_patterns = settings.value('exclude_patterns', [])
        self.exclude_patterns = set(exclude_patterns) if exclude_patterns else set()
        
    def save_settings(self):
        """
        Save application settings.

        This method saves the last directory and exclude patterns to the settings.
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