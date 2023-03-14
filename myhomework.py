import sys
from pathlib import Path
import os
import zipfile
import tarfile

CATEGORIES = {'audio': ['.mp3', '.aiff'],
              'image': ['.png', '.jpg']}

def get_categories(file:Path):
    extension = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if extension in exts:
            return cat
    return 'unknown'

#path = Path(r'd:\testfolder')

#for item in path.glob('**'):
#    print(item)

def move_file(file:Path, root_dir:Path, category:str):
    if category == 'unknown':
        return file.replace(root_dir.joinpath(file.name))

    target_folder = root_dir.joinpath(category)

    if not target_folder.exists():
        target_folder.mkdir()
    return file.replace(target_folder.joinpath(file.name))


def sort_dir(root_dir:Path, current_dir):
    for item in current_dir.glob('*'):
        if not item.is_dir():
            category = get_categories(item)
            new_path = move_file(item, root_dir, category)
            print(new_path)
        else:
            sort_dir(item)
            item.rmdir()
            
def unpack_archives(src_folder):
    archive_folder = os.path.join(src_folder, "archives")
    if not os.path.exists(archive_folder):
        return

    for filename in os.listdir(archive_folder):
        file_path = os.path.join(archive_folder, filename)

        if filename.endswith(".zip"):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(src_folder)
        elif filename.endswith(".tar.gz") or filename.endswith(".tgz"):
            with tarfile.open(file_path, 'r:gz') as tar_ref:
                tar_ref.extractall(src_folder)
        elif filename.endswith(".tar"):
            with tarfile.open(file_path, 'r') as tar_ref:
                tar_ref.extractall(src_folder)

        os.remove(file_path)

def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return f'No path to folder. Take as parametr'
    
    if not path.exists():
        return "Sorry, folder not exist"
    
    sort_dir(path, path)

    return "Everything is ok"
    
if __name__ == "__main__":
    print(main())
    
