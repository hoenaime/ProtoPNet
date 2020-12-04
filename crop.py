"""
Ce fichier sert à découper les images des oiseaux du jeu de données
"""
# Imports de python
from pathlib import Path
from math import floor

# Imports de modules tiers
import cv2
from tqdm import tqdm

# Variables à modifier
dataset_path = 'datasets/CUB_200_2011'
output_folder = 'datasets/cub200_cropped/by_bird'


if __name__ == '__main__':
    dataset_path = Path(dataset_path)
    output_folder = Path(output_folder)
    with open(dataset_path/'images.txt') as img_file, open(dataset_path/'bounding_boxes.txt') as bb_file:
        for img_line, bb_line in tqdm(zip(img_file, bb_file)):
            bb = [floor(float(number)) for number in bb_line.split(' ')[1:]]
            img_location = img_line.split(' ')[1]
            img_path = dataset_path/'images'/img_location
            img = cv2.imread(img_path.as_posix().strip())
            img_cropped = img[bb[1]:bb[1]+bb[3], bb[0]:bb[0]+bb[2]]
            output_path = output_folder/img_location
            output_path.parent.mkdir(parents=True, exist_ok=True)
            cv2.imwrite(output_path.as_posix().strip(), img_cropped)



