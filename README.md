# What does this do?
These scripts are a simple way to take weirdly-named image and video files and attempt to rename them to the date and time they were created. The rename is based off the EXIF metadata.
Example: "IMG_1830.jpeg" -> "2011-07-06 17-00-11.jpeg"
Not all filetypes are supported. This is best used with PNG, JPEG, and MP4 files with proper already-existing EXIF data. It will not create/modify EXIF data. 

# What is the difference with recursive_ ?
The script ```renameImgVidToDateTime.py``` will only rename any immediately-visable images and videos inside the directory. 
The script ```recursive_renameImgVidToDateTime.py``` will do the same, but also look through any folders and sub-folders etc that it can find in the directory. This is potentially dangerous if you run it in a high-level directory such as the root drive of the OS.
**Use at your own risk! Only place this at the root of a folder with your images and videos!**


# Usage:
1) Have Python3 components installed. (Check the imports.)
2) Place the script inside the folder (or folder containing subfolders) containing the images and videos.
3) Linux: Give the script permissions: ```chmod +x renameImgVidToDateTime.py```
4) Run script inside the containing folder from terminal: ```python3 renameImgVidToDateTime.py```
5) Review terminal for any issues.
