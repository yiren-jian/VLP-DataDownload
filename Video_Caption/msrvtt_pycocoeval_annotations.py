import os
import json

original_annotation_file = "/home/yiren/lavis_datasets/msrvtt/annotations/cap_test.json"
new_annotation_file = "/home/yiren/lavis_datasets/msrvtt_gt/msrvtt_cap_test.json"

with open(original_annotation_file) as f:
    original_annotation = json.load(f)

reference = {"annotations": original_annotation}
with open(new_annotation_file, 'w') as f:
    json.dump(reference, f)
