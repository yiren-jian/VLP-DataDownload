import os
import json
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
import multiprocessing as mp
import warnings

from PIL import Image
from decord import VideoReader

### LAVIS cc3m.json
### [{"image": "xxx/yyy/zzz/000000.jpg", "caption": "a cat wearing sunglasses"}, {"image": "xxx/yyy/zzz/000001.jpg", "caption": "a dog wearing sunglasses"}]

def check_images(image_path):
    try:
        vr = VideoReader(url=image_path, height=224, width=224)
        ann_path = image_path.replace("mp4", "json")
        with open(ann_path, 'r') as f:
            ann = json.load(f)
        return image_path, ann["caption"]
    except Exception as e:
        return None


images = []
for root, dirs, files in os.walk("lavis_datasets/webvid2m/train_dataset"):
    for file in files:
        if file.endswith(".mp4"):
            images.append(os.path.join(root, file))

print("Number of images/videos in this dataset: ", len(images))

# finding damage
pool = mp.Pool(cpu_count())
annotations = []

for result in tqdm(pool.imap(check_images, images), total=len(images)):
    if result is None:
        pass
    else:
        annotations.append({"image": result[0], "caption": result[1]})

with open("webvid2m.json", "w") as outputfile:
    json.dump(annotations, outputfile)
