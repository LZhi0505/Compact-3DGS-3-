# python metrics.py -m <path to trained model>
# scene: ['kejiguan', 'linggongtang', 'sipingguzhai', 'wanfota', 'xiangjiadang', 'zhiwu']

import os

for idx, scene in enumerate(['kejiguan', 'linggongtang', 'sipingguzhai', 'wanfota', 'xiangjiadang', 'zhiwu']):
    print('---------------------------------------------------------------------------------')
    one_cmd = f'python metrics.py -m output/{scene}'
    print(one_cmd)
    os.system(one_cmd)