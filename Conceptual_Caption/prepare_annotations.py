import json
import pandas
import os
from tqdm import tqdm
from PIL import Image
from multiprocessing import Pool, cpu_count
import multiprocessing as mp
import warnings


DATA_SPLIT = 'training/' # 'validation/'
# DATA_SPLIT =  'validation/'
# warnings.simplefilter("always")
# warnings.filterwarnings("error")

def check_images(imagePath, file_path = DATA_SPLIT):
    try:
        I = Image.open(file_path + imagePath).convert('RGB')
        return None
    except Exception as e:
        # with open(os.path.join(os.path.join(file_path, log_file)), 'a+') as fp:
        #     fp.write("%s\n" % url)
        # print(imagePath, e)
        return imagePath

if __name__ == "__main__":

    name = "cc3m"
    files_all = os.listdir(DATA_SPLIT)


    if DATA_SPLIT == 'training/':
        df=pandas.read_csv('Train_GCC-training.tsv', header=None, sep='\t')
    else:
        df=pandas.read_csv('Validation_GCC-1.1.0-Validation.tsv', header=None, sep='\t')

    # finding damage
    pool = mp.Pool(cpu_count())
    damaged_files = []

    for result in tqdm(pool.imap(check_images, files_all), total=len(files_all)):
        if result is not None:
            damaged_files.append(result)
    print("damage file len: ", len(damaged_files))
    print("damage file ratio: ", len(damaged_files)/len(files_all))


    all_list = []
    for i in tqdm(files_all):
        if i in damaged_files:
            continue
        line = i.split('_')
        line_num = line[0]
        if '.' in line_num:
            continue

        caption = df.loc[int(line_num)][0]
        all_list.append({"image": '/home/yiren/ssd1/DownloadConceptualCaptions/' + DATA_SPLIT + i, "caption":caption})

    if DATA_SPLIT == 'training/':
        with open(name + "_training.json", "w") as outfile:
            json.dump(all_list, outfile)
    else:
        with open(name + "_validation.json", "w") as outfile:
            json.dump(all_list, outfile)
