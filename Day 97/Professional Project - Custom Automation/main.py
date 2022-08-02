import os
import shutil


downloads_folder = "C:/Users/USER/Downloads"
videos_folder = "C:/Users/USER/Videos"


print("\nStarting program...\n")
for item in os.scandir(downloads_folder):
    if item.is_dir():
        pass
    else:
        print(f"Moving {item.name}")
        if item.path.endswith(".mp4") or item.path.endswith(".mkv"):
            shutil.move(item.path, videos_folder)
        if item.path.endswith(".srt"):
            shutil.move(item.path, f"{videos_folder}/Subtitles")

print("\nAll done!\n")