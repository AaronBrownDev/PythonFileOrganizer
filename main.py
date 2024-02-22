from configparser import ConfigParser
import os

config = ConfigParser()
config.read("file_locations.ini")

file_locations = {
    "b_directory" : config["DEFAULT"]["beginning_direct"],
    "archives" : config["DEFAULT"]["beginning_direct"] + "/Archives",
    "documents" : config["DEFAULT"]["beginning_direct"] + "/Documents",
    "images" : config["DEFAULT"]["beginning_direct"] + "/Images",
    "videos" : config["DEFAULT"]["beginning_direct"] + "/Videos",
    "audio" : config["DEFAULT"]["beginning_direct"] + "/Audio",
    "code" : config["DEFAULT"]["beginning_direct"] + "/Code",
    "executables" : config["DEFAULT"]["beginning_direct"] + "/Executables",
    "system_files" : config["DEFAULT"]["beginning_direct"] + "/System Files",
    "other" : config["DEFAULT"]["beginning_direct"] + "/Other"
}

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


def main():
    with os.scandir(file_locations.get("b_directory")) as directory:
        for path in directory:
            if path.is_file():
                file_name = path.name
                file_extension = f".{path.name.split(".")[-1]}"
                for group in file_extensions:
                    if file_extension in file_extensions[group]:
                        print(group, file_extension)
                        
if __name__ == "__main__":
    main()