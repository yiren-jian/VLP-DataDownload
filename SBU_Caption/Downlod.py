import sys, os
import requests
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from functools import partial

headers = {
    #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'User-Agent':'Googlebot-Image/1.0', # Pretend to be googlebot
    'X-Forwarded-For': '64.18.15.200'
}

file_path = os.path.dirname(os.path.abspath(__file__))
log_file = 'log.txt'

def download_images(url, filePath):
    try:
        file_name = url.split("/")[-2] + '_' + url.split("/")[-1]
        response = requests.get(url, stream=False, timeout=10, allow_redirects=True, headers=headers)
        # print(" Downloaded {} ".format(file_name))
        savePath = os.path.join(os.path.join(filePath, file_name))
        with open(savePath, 'wb') as f:
            f.write(response.content)

    except Exception as e:
        with open(os.path.join(os.path.join(file_path, log_file)), 'a+') as fp:
            fp.write("%s\n" % url)
        print(e)


if __name__ == "__main__":
    # read file
    with open('SBU_captioned_photo_dataset_urls.txt') as f:
        lines = f.readlines()
    webs = [line.replace('\n', '') for line in lines]

    directory = 'sbu_images'
    if not os.path.exists(directory):
        os.makedirs(directory)


    filePath = os.path.join(os.path.join(file_path, directory))
    print("filePath is %s " % filePath)


    print("There are {} CPUs on this machine ".format(cpu_count()))
    pool = Pool(cpu_count())
    result_list_tqdm = []
    download_func = partial(download_images, filePath = filePath)
    for result in tqdm(pool.imap(download_func, webs), total=len(webs)):
        result_list_tqdm.append(result)
    # results = pool.map(download_func, webs)
    pool.close()
    pool.join()

