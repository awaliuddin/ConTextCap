#!/usr/bin/env python3

import sys
import os
from pathlib import Path
from typing import Optional
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QPushButton, QTextEdit, QFileDialog, QProgressDialog,
    QMessageBox
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import fpdf
import mimetypes

class DirectoryScanner(QThread):
    """Worker thread for scanning directories"""
    progress = pyqtSignal(int)
    structure_ready = pyqtSignal(str)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, root_path: str):
        super().__init__()
        self.root_path = root_path
        self.total_items = 0
        self.processed_items = 0

    def run(self):
        try:
            # First pass to count items for progress
            for _ in Path(self.root_path).rglob('*'):
                self.total_items += 1

            # Generate directory structure
            structure = []
            for current_path in Path(self.root_path).rglob('*'):
                try:
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
    """Worker thread for PDF generation"""
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error_occurred = pyqtSignal(str)
    
    def __init__(self, root_path: str, output_path: str):
        super().__init__()
        self.root_path = root_path
        self.output_path = output_path
        self.total_files = 0
        self.processed_files = 0

    def run(self):
        try:
            # Count total files first
            for _ in Path(self.root_path).rglob('*'):
                if _.is_file():
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
                if file_path.is_file():
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
        super().__init__()
        self.selected_path: Optional[str] = None
        self.initUI()

    def initUI(self):
        """Initialize the user interface"""
        self.setWindowTitle('Codebase Capture')
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create buttons
        set_location_btn = QPushButton('Set Codebase Location')
        create_pdf_btn = QPushButton('Create PDF')
        
        # Create text display area
        self.structure_display = QTextEdit()
        self.structure_display.setReadOnly(True)

        # Add widgets to layout
        layout.addWidget(set_location_btn)
        layout.addWidget(create_pdf_btn)
        layout.addWidget(self.structure_display)

        # Connect signals
        set_location_btn.clicked.connect(self.select_directory)
        create_pdf_btn.clicked.connect(self.create_pdf)

    def select_directory(self):
        """Handle directory selection"""
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
        """Handle PDF creation"""
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
        """Display the directory structure"""
        self.structure_display.setText(structure)

    def show_error(self, message: str):
        """Display error message"""
        QMessageBox.critical(self, "Error", message)

def main():
    # Initialize application
    app = QApplication(sys.argv)
    
    # Create and show main window
    window = CodebaseCaptureWindow()
    window.show()
    
    # Start event loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()