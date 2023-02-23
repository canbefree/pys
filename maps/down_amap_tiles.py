import itertools
import requests
import math
import os
import numpy as np


# define the URL for tile server and get the proper size of the image, this example shows China
URL = "http://webrd04.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scale=1&style=7"

if not os.path.isdir("./tiles"):
    os.makedirs("./tiles", 0o777)


def download_tile(x, y, z):
    if not os.path.isdir(f"./tiles/{z}"):
        os.makedirs(f"./tiles/{z}", 0o777)
    file = f"./tiles/{z}/{x}_{y}.png"
    print(f"download:{file}")
    if os.path.exists(file) == True:
        print(f"download:{file} file exist")
        return
    url = URL.format(x=x, y=y, z=z)
    r = requests.get(url)
    if r.status_code == 200:
        with open(file, 'wb') as f:
            f.write(r.content)

# Python Script to Calculate ZXY
def calc_zxy(lat, long, zoom):
    n = 2 ** zoom
    x = (long + 180) / 360 * n
    y = (1 - math.log(math.tan(lat * math.pi / 180) + 1 /
         math.cos(lat * math.pi / 180)) / math.pi) / 2 * n
    return int(zoom), int(x), int(y)

def down_all():
    for k, i, j in itertools.product(range(5, 8), range(-89, 90), range(-179, 180)):
        z, x, y = calc_zxy(i, j, k)
        download_tile(x, y, z)

# def down_area(local1,local2,zoom):
    # for i in range(0,zoom):
    #     z = i+1
    #     calc1 = calc_zxy(local1,zoom)


