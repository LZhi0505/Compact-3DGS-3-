# python render.py -m <path to trained model> --max_hashmap <max hash size of the model>
# scene: ['kejiguan', 'wanfota', 'zhiwu', 'linggongtang', 'xiangjiadang', 'sipingguzhai']

import os

for cuda, scene in enumerate(['kejiguan', 'zhiwu', 'linggongtang']):
    one_cmd = f'python render.py -m output/{scene} --max_hashmap 19'
    os.system(one_cmd)