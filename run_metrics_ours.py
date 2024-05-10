# python metrics.py -m <path to trained model>
# scene: ['kejiguan', 'wanfota', 'zhiwu', 'linggongtang', 'xiangjiadang', 'sipingguzhai']

import os

for cuda, scene in enumerate(['kejiguan', 'wanfota', 'zhiwu']):
    one_cmd = f'python metrics.py -m output/{scene}'
    os.system(one_cmd)