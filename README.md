# My Own Tools for Extracting Work and Organizing Files

## Project Overview
This project provides a command-line tool for managing and organizing work-related files, specifically designed to streamline tasks such as exporting WordPress themes. The tool offers a simple, user-friendly interface for selecting and executing various methods.

## Features
- **ASCII Art Display**: Show a welcome message with stylish ASCII art using `pyfiglet`.
- **Method Selection**: Display a list of available methods for the user to choose from.
- **Theme Export**: A dedicated method (`wpet`) for exporting a WordPress theme, prompting the user to enter the theme path and handling input validation.

## Installation
To use this tool, clone the repository and ensure you have Python installed with `pyfiglet`:

```bash
git clone https://github.com/Eslam1811477/indev
cd indev
pip freeze > requirements.txt
pip install -r requirements.txt
pip install

python -m PyInstaller --add-data "C:\\Users\\eslam\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\site-packages\\pyfiglet/fonts;pyfiglet/fonts" --onefile --icon=ex.ico indev.py