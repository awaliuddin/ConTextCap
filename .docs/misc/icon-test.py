#!/usr/bin/env python3

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,
    QStyle, QFileIconProvider
)
from PyQt6.QtCore import QFileInfo
from pathlib import Path
import sys

class IconTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('System Icons Test')
        self.setGeometry(100, 100, 400, 600)
        
        # Create tree widget
        self.tree = QTreeWidget()
        self.tree.setHeaderLabel('File Types')
        self.setCentralWidget(self.tree)
        
        # Get system style for icons
        self.style = QApplication.style()
        
        # Add some common file types
        self.add_file_types()
        
    def add_file_types(self):
        # Add folder
        folder_item = QTreeWidgetItem(self.tree)
        folder_item.setText(0, "Folder")
        folder_item.setIcon(0, self.style.standardIcon(QStyle.StandardPixmap.SP_DirIcon))
        
        # Add common file types with system icons
        file_types = [
            ("Text File", QStyle.StandardPixmap.SP_FileIcon),
            ("Python File", QStyle.StandardPixmap.SP_FileIcon),
            ("PDF Document", QStyle.StandardPixmap.SP_FileIcon),
            ("Image File", QStyle.StandardPixmap.SP_FileIcon),
            ("HTML File", QStyle.StandardPixmap.SP_FileIcon)
        ]
        
        for name, icon_type in file_types:
            item = QTreeWidgetItem(self.tree)
            item.setText(0, name)
            item.setIcon(0, self.style.standardIcon(icon_type))

def main():
    app = QApplication(sys.argv)
    window = IconTestWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()