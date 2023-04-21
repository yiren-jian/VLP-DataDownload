import json
import pandas
from tqdm import tqdm
import os
from PIL import Image
from multiprocessing import Pool, cpu_count
import multiprocessing as mp
import warnings


WORKING_FILE_PATH = './'
def check_images(imagePath, file_path = WORKING_FILE_PATH):
    # print(file_path + imagePath)
    try:
        I = Image.open(file_path + imagePath).convert('RGB')
        return None
    except Exception as e:
        return imagePath

if __name__ == "__main__":

    name = "sbu"
    dataset = pandas.read_csv("meta.csv")


    image_path = dataset['path'].values.tolist()
    captions = dataset['captions'].values.tolist()

    # # finding damage
    # pool = mp.Pool(cpu_count())
    # damaged_files = []
    #
    # for result in tqdm(pool.imap(check_images, image_path), total=len(image_path)):
    #     if result is not None:
    #         damaged_files.append(result)
    # print("damage file len: ", len(damaged_files))
    # print("damage file ratio: ", len(damaged_files)/len(image_path))

    all_list = []
    for i in tqdm(range(len(image_path))):
        all_list.append({"image": "/home/yiren/ssd1/SBU_Captions_Dataset_Download/" + image_path[i], "caption":captions[i]})

    with open(name + ".json", "w") as outfile:
        json.dump(all_list, outfile)
