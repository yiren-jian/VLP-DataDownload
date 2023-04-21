import json
import os
from tqdm import tqdm

if __name__ == '__main__':
    with open('old_json/vg.json') as f:
       vg = json.load(f)

    new_vg = []
    old_path = "/export/share/datasets/vision/visual-genome/image"
    new_path = "/home/yiren/ssd1/VisualGenome-1.2/images"
    for pair in tqdm(vg):
        new_vg.append({"image": pair["image"].replace(old_path, new_path), "caption": pair["caption"]})

    with open("vg.json", "w") as outfile:
        json.dump(new_vg, outfile)

    with open('old_json/coco.json') as f:
       coco = json.load(f)

    new_coco = []
    old_path = "/export/share/datasets/vision/coco/images"
    new_path = "/home/yiren/ssd1/MSCOCO"
    for pair in tqdm(coco):
        new_coco.append({"image": pair["image"].replace(old_path, new_path), "caption": pair["caption"]})

    with open("coco.json", "w") as outfile:
        json.dump(new_coco, outfile)
