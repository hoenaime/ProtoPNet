"""
Ce fichier sert à séparer le jeu de donnée
"""
# Imports de python
from pathlib import Path
import shutil

# Import de modules tiers
from tqdm import tqdm

# Variables à modifier
dataset_path = 'datasets/CUB_200_2011'
dataset_cropped_path = 'datasets/cub200_cropped/by_bird'

if __name__ == '__main__':
    dataset_cropped_path = Path(dataset_cropped_path)
    dataset_path = Path(dataset_path)
    train_folder = Path('datasets/cub200_cropped/train_cropped')
    test_folder = Path('datasets/cub200_cropped/test_cropped')
    with open(dataset_path/'images.txt') as img_file, open(dataset_path/'train_test_split.txt') as test_train_file:
        for img_line, test_train_line in tqdm(zip(img_file, test_train_file)):
            img_location = img_line.split(' ')[1]
            img_path = dataset_cropped_path / img_location
            is_training_img = int(test_train_line.split(" ")[1]) == 1
            if is_training_img:
                output_location = train_folder / img_location
            else:
                output_location = test_folder / img_location
            output_location.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(img_path.as_posix().strip(), output_location.as_posix().strip())
