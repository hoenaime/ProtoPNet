"""
Ce fichier sert à séparer le jeu de donnée
"""
# Imports de python
from pathlib import Path
import shutil

# Import de modules tiers
from tqdm import tqdm

# Variables à modifier
dataset_path = 'datasets/MIT'
dataset_cropped_path = 'datasets/MIT/Images'

if __name__ == '__main__':
    dataset_cropped_path = Path(dataset_cropped_path)
    dataset_path = Path(dataset_path)
    train_folder = Path('datasets/MIT/train')
    test_folder = Path('datasets/MIT/test')
    for is_training_img, filename in ((True, 'TrainImages.txt'), (False, 'TestImages.txt')):
        with open(dataset_path/filename) as img_file:
            for img_line in tqdm(img_file):
                img_location = img_line
                img_path = dataset_cropped_path / img_location
                if is_training_img:
                    output_location = train_folder / img_location
                else:
                    output_location = test_folder / img_location
                output_location.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(img_path.as_posix().strip(), output_location.as_posix().strip())


