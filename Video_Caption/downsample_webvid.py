import os
import json
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
import multiprocessing as mp

import ffmpeg
import warnings

def downsample_images(image_path):
    try:
        vr = ffmpeg.input(image_path).filter("setpts", "0.1*PTS")
        save_dir = os.path.split(image_path.replace("dataset", "dataset_downsampled"))[0]
        if not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)
        ffmpeg.output(vr, imagepath.replace("dataset", "dataset_downsampled"), loglevel="quiet").run(overwrite_output=True)
    except Exception as e:
        return image_path

images = []
for root, dirs, files in os.walk("lavis_datasets/webvid2m/train_dataset"):
    for file in files:
        if file.endswith(".mp4"):
            images.append(os.path.join(root, file))

print("Number of images/videos in this dataset: ", len(images))

pool = mp.Pool(cpu_count())

for result in tqdm(pool.imap(downsample_images, images), total=len(images)):
    if result is None:
        pass
    else:
        warnings.warn(f"Failed to downsample eanmples with video: {result}.")
