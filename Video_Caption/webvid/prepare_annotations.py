import os
import pandas as pd
import json
from tqdm import tqdm


if __name__ == '__main__':
    annotations = []
    not_found = []
    df = pd.read_csv("results_2M_train_1/0.csv")

    for index, row in tqdm(df.iterrows()):
        video = os.path.join(str(row["page_dir"]), str(row["videoid"]) + ".mp4")
        caption = row["name"]
        if os.path.isfile(os.path.join("data/videos", video)):
            annotations.append({"image": os.path.join("data/videos", video), "caption": caption})
        else:
            not_found.append(video)

    with open("webvid2m.json", "w") as outputfile:
        json.dump(annotations, outputfile)

    print(len(annotations), len(not_found))
