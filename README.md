# PythonFileOrganizer
A simple and effective Python script to declutter your directories.

Features

    Easy to use - customize file organization with a simple configuration file.
    Handles file type identification for sorting into designated folders.
    Manages duplicate files to prevent overwriting.

Prerequisites

    Python 3.x (https://www.python.org/)

Installation

    Download or clone the project files:
        file_organizer.py (Your main Python script)
        file_locations.ini (Configuration file)

    Install required Python module:
    Bash

    pip install configparser

    Use code with caution.

Configuration

    Open file_locations.ini

    Under the [DEFAULT] section, modify the source_directory value:
    Ini, TOML

    [DEFAULT]
    source_directory = /your/desired/source/directory 

    Use code with caution.

        Replace /your/desired/source/directory with the actual path to the directory you want to organize.

Usage

    Run the script:
    Bash

    python file_organizer.py

    Use code with caution.

How it Works

    The script reads the configuration in file_locations.ini.
    It scans the specified source_directory.
    Identifies file types based on their extensions.
    Assigns files to corresponding folders (e.g., "Images", "Documents," etc.).
    Creates folders if they don't exist.
    Handles potential duplicate filenames.

Customization

You can customize the organization scheme by:

    Editing file_locations.ini: Add or modify folder paths.
    Modifying file_extensions dictionary: Add or change file extensions and their associated categories.

Important Notes

    It's recommended to test the script on a sample directory before organizing a large collection of files.
    Always create a backup of important data before running organization scripts.

