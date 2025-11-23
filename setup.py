#!/usr/bin/env python3
"""
Setup script for ConTextCap.

This script allows the package to be installed using pip.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the long description from README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="contextcap",
    version="1.0.0",
    author="Asif Waliuddin",
    author_email="awaliuddin@example.com",
    description="A powerful desktop application that captures and documents your project codebase",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/awaliuddin/ConTextCap",
    project_urls={
        "Bug Tracker": "https://github.com/awaliuddin/ConTextCap/issues",
        "Documentation": "https://github.com/awaliuddin/ConTextCap#readme",
        "Source Code": "https://github.com/awaliuddin/ConTextCap",
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    py_modules=["ConTextCap"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Documentation",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyQt6>=6.4.0",
        "fpdf2>=2.7.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-qt>=4.2.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
            "bandit>=1.7.5",
            "safety>=2.3.5",
            "pre-commit>=3.4.0",
        ],
        "docs": [
            "pdoc3>=0.10.0",
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "contextcap=ConTextCap:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["icons/**/*", "fonts/**/*"],
    },
    keywords="documentation pdf codebase developer-tools llm",
    zip_safe=False,
)
