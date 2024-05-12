# python train.py -s ../../Dataset/3DGS_Dataset/sipingguzhai --model_path output/sipingguzhai --resolution 1 --data_device "cuda --store_npz"
# scene: {'kejiguan': 'cuda', 'linggongtang': 'cuda', 'sipingguzhai': 'cpu', 'wanfota': 'cuda', 'xiangjiadang': 'cuda', 'zhiwu': 'cuda'}

import os

for idx, scene in enumerate({'kejiguan': 'cuda', 'linggongtang': 'cuda', 'sipingguzhai': 'cpu', 'wanfota': 'cuda', 'xiangjiadang': 'cuda', 'zhiwu': 'cuda'}.items()):
    print('---------------------------------------------------------------------------------')
    one_cmd = f'python train.py -s ../../Dataset/3DGS_Dataset/{scene[0]} --model_path output/{scene[0]} --resolution 1 --data_device "{scene[1]}" --store_npz'
    print(one_cmd)
    os.system(one_cmd)

for idx, scene in enumerate(['kejiguan', 'linggongtang', 'sipingguzhai', 'wanfota', 'xiangjiadang', 'zhiwu']):
    print('---------------------------------------------------------------------------------')
    one_cmd = f'python render.py -m output/{scene} --max_hashmap 19'
    print(one_cmd)
    os.system(one_cmd)

for idx, scene in enumerate(['kejiguan', 'linggongtang', 'sipingguzhai', 'wanfota', 'xiangjiadang', 'zhiwu']):
    print('---------------------------------------------------------------------------------')
    one_cmd = f'python metrics.py -m output/{scene}'
    print(one_cmd)
    os.system(one_cmd)