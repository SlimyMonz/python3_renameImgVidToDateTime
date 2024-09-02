import os
import mimetypes
import exifread
from datetime import datetime
from exifread.heic import NoParser

def is_image_or_video(file):
    mimetype, _ = mimetypes.guess_type(file)
    return mimetype and (mimetype.startswith('image/') or mimetype.startswith('video/'))

def process_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            tags = exifread.process_file(f, details=False)
        if 'EXIF DateTimeOriginal' in tags:
            datetime_original = datetime.strptime(str(tags['EXIF DateTimeOriginal']), "%Y:%m:%d %H:%M:%S")
            new_filename = datetime_original.strftime("%Y-%m-%d %H-%M-%S") + os.path.splitext(filepath)[1]
            new_filepath = os.path.join(os.path.dirname(filepath), new_filename)
            os.rename(filepath, new_filepath)
        else:
            print(f"DateTimeOriginal tag not found for file: {filepath}")
    except NoParser:
        print(f"Could not parse EXIF data for file: {filepath}")
    except Exception as e:
        print(f"Error processing file {filepath}: {e}")

def process_directory(root_directory):
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if is_image_or_video(file_path):
                process_file(file_path)

if __name__ == "__main__":
    current_working_directory = os.getcwd()
    process_directory(current_working_directory)
