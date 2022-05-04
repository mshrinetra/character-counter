import os
from datetime import datetime


def clear_path(file_path):

  # Check whether the specified path exists or not
  dirExists = os.path.exists(os.path.dirname(file_path))

  if not dirExists:
    # Create a new directory because it does not exist 
    os.makedirs(os.path.dirname(file_path), exist_ok=False)
    print("The new directory is created!")

  fileExists = os.path.exists(file_path)

  if fileExists:
    newName = os.path.join(os.path.dirname(file_path), datetime.now().strftime("%d%m%y%H%M%S") + os.path.basename(file_path));
    os.rename(file_path, newName)
    print("Old file backed up")
