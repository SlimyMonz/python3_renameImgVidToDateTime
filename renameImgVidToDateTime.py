import os
import mimetypes
import exifread
from datetime import datetime
from exifread.heic import NoParser

current_working_directory = os.getcwd()


def is_image_or_video(file):
    mimetype, _ = mimetypes.guess_type(file)
    return mimetype and (mimetype.startswith('image/') or mimetype.startswith('video/'))


for filename in os.listdir(current_working_directory):
    if is_image_or_video(filename):
        try:
            with open(filename, 'rb') as f:
                tags = exifread.process_file(f, details=False)
            if 'EXIF DateTimeOriginal' in tags:
                datetime_original = datetime.strptime(str(tags['EXIF DateTimeOriginal']), "%Y:%m:%d %H:%M:%S")
                new_filename = datetime_original.strftime("%Y-%m-%d %H-%M-%S") + os.path.splitext(filename)[1]
                os.rename(os.path.join(current_working_directory, filename),
                          os.path.join(current_working_directory, new_filename))
            else:
                print("DateTimeOriginal tag not found")
        except NoParser:
            print(f"Could not parse EXIF data for file: {filename}")
        except Exception as e:
            print(f"Error processing file {filename}: {e}")
