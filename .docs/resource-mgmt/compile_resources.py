#!/usr/bin/env python3

import os
import subprocess
import sys

def compile_resources():
    """Compile Qt resources into Python module"""
    try:
        # Try to import PyQt6 to get its location
        import PyQt6
        pyqt_dir = os.path.dirname(PyQt6.__file__)
        
        # Find rcc.exe in the PyQt6 directory
        rcc_path = os.path.join(pyqt_dir, 'Qt6', 'bin', 'rcc.exe')
        
        if not os.path.exists(rcc_path):
            print(f"Error: rcc.exe not found at {rcc_path}")
            return False
            
        # Compile resources.qrc to resources_rc.py
        cmd = [rcc_path, "resources.qrc", "-o", "resources_rc.py"]
        subprocess.run(cmd, check=True)
        print("Resources compiled successfully!")
        return True
        
    except ImportError:
        print("Error: PyQt6 not found. Please install PyQt6 first.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error compiling resources: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == '__main__':
    sys.exit(0 if compile_resources() else 1)
