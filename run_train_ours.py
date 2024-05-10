# python train.py -s /media/liuzhi/b4608ade-d2e0-430d-a40b-f29a8b22cb8c/Dataset/3DGS_Dataset/科技馆 --model_path output/kejiguan --eval --resolution 1
# scene: {'科技馆': 'kejiguan', '万佛塔': 'wanfota', '植物': 'zhiwu', '凌公塘': 'linggongtang', '湘家荡': 'xiangjiadang', '寺平古宅': 'sipingguzhai'}

import os

for cuda, scene in enumerate({'湘家荡': 'xiangjiadang', '寺平古宅': 'sipingguzhai'}):
    one_cmd = f'python train.py -s /media/liuzhi/b4608ade-d2e0-430d-a40b-f29a8b22cb8c/Dataset/3DGS_Dataset/{scene[0]} --model_path output/{scene[1]} --eval --resolution 1'
    os.system(one_cmd)