import os
import shutil
from configparser import ConfigParser
from pathlib import Path

config = ConfigParser()
config.read("file_locations.ini")

# file locations of source and output directories
file_locations = {
    "src_directory": config["DEFAULT"]["beginning_direct"],
    "Archives": config["DEFAULT"]["beginning_direct"] + "Archives",
    "Documents": config["DEFAULT"]["beginning_direct"] + "Documents",
    "Images": config["DEFAULT"]["beginning_direct"] + "Images",
    "Videos": config["DEFAULT"]["beginning_direct"] + "Videos",
    "Audio": config["DEFAULT"]["beginning_direct"] + "Audio",
    "Code": config["DEFAULT"]["beginning_direct"] + "Code",
    "Executables": config["DEFAULT"]["beginning_direct"] + "Executables",
    "System_files": config["DEFAULT"]["beginning_direct"] + "System Files",
    "Other": config["DEFAULT"]["beginning_direct"] + "Other"
}

# assigns the file extensions into groups by their umbrella type
file_extensions = {
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Documents": [".doc", ".docx", ".pdf", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".ogg", ".aac", ".flac"],
    "Code": [".py", ".java", ".js", ".html", ".css", ".c", ".cpp", ".php", ".sql"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".app"],
    "System Files": [".dll", ".sys", ".tmp", ".log"],
}


# gives the file a folder to go into
def assign_file(path):
    file_extension = f".{path.name.split('.')[-1]}"
    folder = "Other"  # initialize the folder as other in case file type is not listed

    for group in file_extensions:
        if file_extension in file_extensions[group]:
            folder = group

    return folder


def handle_duplicate(file, folder):
    while file.name in os.listdir(file_locations.get(folder)):
        print(file.name)
        print(file)
        dst = ''.join(file.name.split('.')[:-1] + ["-duplicate."] + [file.name.split('.')[-1]])
        os.rename(src=file, dst=config["DEFAULT"]["beginning_direct"]+dst)
        file = Path(config["DEFAULT"]["beginning_direct"]+dst)

    return file


# moves the file into its assigned folder    
def move_file(file, folder):
    if not os.path.exists(file_locations[folder]):
        # creates the folder when the folder does not exist in the source directory
        os.makedirs(file_locations[folder])

    file = handle_duplicate(file, folder)
    shutil.move(file, file_locations[folder])


def main():
    # Goes through the source directory
    with os.scandir(file_locations.get("src_directory")) as directory:
        for path in directory:
            if path.is_file():
                folder = assign_file(path)
                move_file(path, folder)


if __name__ == "__main__":
    main()
