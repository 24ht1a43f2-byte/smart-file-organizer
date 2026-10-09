
from pathlib import Path
import shutil

print("Welcome to Smart File Organizer!")

folder_input = input("Enter the folder path to organize: ")
folder = Path(folder_input.strip().strip('"'))

if not folder.is_dir():
    print("Invalid folder path. Please try again.")
    raise SystemExit

file_types = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"]
}

count = 0

for file in list(folder.iterdir()):
    if not file.is_file():
        continue

    category = "Others"

    for name, extensions in file_types.items():
        if file.suffix.lower() in extensions:
            category = name
            break

    destination_folder = folder / category
    destination_folder.mkdir(exist_ok=True)

    destination = destination_folder / file.name

    if destination.exists():
        print(f"Skipped duplicate: {file.name}")
        continue

    try:
        shutil.move(str(file), str(destination))
        print(f"Moved {file.name} to {category}")
        count += 1
    except OSError as error:
        print(f"Could not move {file.name}: {error}")

print(f"\nDone! Organized {count} files.")