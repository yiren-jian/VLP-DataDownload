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