import os
from os import listdir
from os.path import isfile, join, isdir

if __name__ == '__main__':

    parent_dir = "data/videos"
    dirs = [join(parent_dir, name) for name in listdir(parent_dir) if isdir(join(parent_dir, name))]
    onlyfiles = []

    for dir in dirs:
        f = [join(dir, f) for f in listdir(dir) if isfile(join(dir, f))]
        onlyfiles += f

    print(onlyfiles)


# data/videos/010851_010900/1062918058.mp4.tmp
# data/videos/026251_026300/6552059.mp4.tmp
# data/videos/067351_067400/1035591560.mp4.tmp
# data/videos/007901_007950/33800158.mp4.tmp
# data/videos/096001_096050/3742148.mp4.tmp
# data/videos/104651_104700/10681772.mp4.tmp
# data/videos/126851_126900/4422923.mp4.tmp
# data/videos/016201_016250/21196966.mp4.tmp
# data/videos/003001_003050/13457234.mp4.tmp
# data/videos/075451_075500/2416907.mp4.tmp
# data/videos/000901_000950/21588649.mp4.tmp
# data/videos/072251_072300/1039963160.mp4.tmp
# data/videos/123951_124000/1010219555.mp4.tmp
# data/videos/002351_002400/6315860.mp4.tmp
# data/videos/030751_030800/3741062.mp4.tmp
# data/videos/017701_017750/22643860.mp4.tmp
# data/videos/026901_026950/3742151.mp4.tmp
# data/videos/079651_079700/474649.mp4.tmp
# data/videos/002401_002450/7412620.mp4.tmp
# data/videos/007951_008000/29160919.mp4.tmp
