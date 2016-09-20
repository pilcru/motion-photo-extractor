#!/usr/bin/env python

import argparse
from pathlib import Path

def parse_options():
    parser = argparse.ArgumentParser(description='Split Samsung GS7 motion photos into separate picture and movie files')
    parser.add_argument("path", nargs="*", default='.', type=Path, 
        help="Paths of the image / folder of images you want to extract the motion from",
        )

    n = parser.parse_args()
    path = n.path
    print("Path: " + str(path))
    return path

def extract_and_save(file):
    with file.open('rb') as f:
        data = f.read()
        parts = data.split(b"MotionPhoto_Data", maxsplit=1)
    
    if len(parts) == 2:
        file_image = file.parent / (file.stem + '_Extracted.jpg')
        file_movie = file.parent / (file.stem + '_Extracted.mp4')
        with file_image.open('wb') as fi:
            fi.write(parts[0])
        with file_movie.open('wb') as fm:
            fm.write(parts[1])
        print(str(file.name + ' - Split'))
    else:
        print(str(file.name) + ' - Not a MotionPhoto')

def process_images(path):
    if isinstance(path, list):
        for path_i in path:
            process_images(path_i)
            return
            
    if path.is_file():
        extract_and_save(path)
    else:
        for file in path.glob('*.jpg'):
            extract_and_save(file)


if __name__ == "__main__":
    process_images(parse_options())
