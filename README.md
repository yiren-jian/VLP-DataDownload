## VLP Data Download

### Conceptual Caption
`download_data.py` download images into `validation` and `training` folder using filenames defined as:

```python
def _file_name(row):
    return "%s/%s_%s" % (row['folder'], row.name, (zlib.crc32(row['url'].encode('utf-8')) & 0xffffffff))
```

e.g.,

```bash
-rw-rw-r-- 1 yiren yiren    62770 Jan 11 23:21 9975_2564971897
-rw-rw-r-- 1 yiren yiren    35190 Jan 11 23:21 997_558016774
-rw-rw-r-- 1 yiren yiren    55242 Jan 11 23:21 9976_960417839
-rw-rw-r-- 1 yiren yiren    36676 Jan 11 23:21 9977_3176616088
-rw-rw-r-- 1 yiren yiren    23328 Jan 11 23:21 9978_586229838
-rw-rw-r-- 1 yiren yiren    77029 Jan 11 23:21 9979_1727102189
-rw-rw-r-- 1 yiren yiren    80234 Jan 11 23:21 9980_2284275823
-rw-rw-r-- 1 yiren yiren    71307 Jan 11 23:21 9982_1890805680
```

`prepare_annotations.py` will validate images by `Image.open().convert('RGB')` and save a json file as annotations used in ALBEF.


### SBU Caption
`Download_new.py` will download images and save a `meta.csv` file with `image_path, caption`:

```bash
sbu_images/4095_4898927440_5c8800ac69.jpg,New curtain for window over kitchen sink
sbu_images/1049_1325996189_e99abf6ced.jpg,Dad and Lukie walking in the water
sbu_images/3333_4640771555_10735f3068.jpg,And the winning horse gets a bucket of water thrown over it!.
sbu_images/1147_1447704653_df10d8c099.jpg,"The girl in the blue dress is our cousin, Lynda."
```
It seems that all images are validated, and `prepare_annotations.py` saves a json file as annotations used in ALBEF.

### LAVIS
Using LAVIS helper to download dataset like SBU (or even CC3m and CC12m) may require data [validating](https://github.com/salesforce/LAVIS/issues/44).

```python
import tqdm
import os
nonvalid_records=[]
valid_records=[]
with open('sbu_captions/annotations/sbu.json', "r") as f:
    dset=json.load(f)
    def check_file_exists(filename,path):
        exist=os.path.exists(os.path.join(path,filename))
        return exist

    for ann in tqdm.tqdm(dset):
        exist=check_file_exists(ann['image'],'sbu_captions/images')

        if exist:
            valid_records.append(ann)
        else:
            nonvalid_records.append(ann)
    print('not valid records',len(nonvalid_records),'valid records',len(valid_records))

print("saving valid")
with open('sbu_captions/annotations/sbu_valid.json', "w") as f:
    dset=json.dump(valid_records,f)

print("saving nonvalid")
with open('sbu_captions/annotations/sbu_nonvalid.json', "w") as f:
    dset=json.dump(nonvalid_records,f)
```

### Misc
Some annotations (VG, CC3m, CC12m) use absolute path that requires special care when training on other machines.
```python
import json

annotation_file = '/tank/local/cgo5577/lavis_datasets/conceptual_caption/annotations/cc3m.json'
old_path = '/home/yiren'
new_path = '/tank/local/cgo5577'

with open(annotation_file, 'r') as f:
  data = json.load(f)

for i in range(len(data)):
  data[i]['image'] = data[i]['image'].replace(old_path, new_path)

with open(annotation_file, 'w') as json_file:
  json.dump(data, json_file)

```

### Flickr30k Caption

Converting LAVIS downloaded Flickr30k to Flickr30k Captioning dataset.
```python
import json

ann_path = "train.json"
with open(ann_path, 'r') as f:
    ann = json.load(f)

new_ann = []
for item in ann:
    img = item["image"]
    for cap in item["caption"]:
        new_ann.append({"img_id": img, "caption":cap, "image": img})

new_ann = {"annotations": new_ann}
with open("train_cap.json", "w") as outputfile:
    json.dump(new_ann, outputfile)
```

### Acknowledgement
Thanks for original implementations of [DownloadConceptualCaptions](https://github.com/igorbrigadir/DownloadConceptualCaptions)
