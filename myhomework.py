import re
import os


def normalize(filename):
     invalid_chars = r'[^\w\d.]'
     translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
        'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'i', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya'
    }
     filename = re.sub(invalid_chars, '_', filename)
     for cyrillic, latin in translit_dict.items():
        filename = filename.replace(cyrillic, latin)

     return filename

import shutil


def sort_files(directory):
    image_dir = os.path.join(directory, 'images')
    document_dir = os.path.join(directory, 'documents')
    audio_dir = os.path.join(directory, 'audio')
    video_dir = os.path.join(directory, 'video')
    archive_dir = os.path.join(directory, 'archives')
    for d in [image_dir, document_dir, audio_dir, video_dir, archive_dir]:
        if not os.path.exists(d):
            os.mkdir(d)