# python render.py -m <path to trained model> --max_hashmap <max hash size of the model>
# scene: ['kejiguan', 'linggongtang', 'sipingguzhai', 'wanfota', 'xiangjiadang', 'zhiwu']

import os

for idx, scene in enumerate(['kejiguan', 'linggongtang', 'sipingguzhai', 'wanfota', 'xiangjiadang', 'zhiwu']):
    print('---------------------------------------------------------------------------------')
    one_cmd = f'python render.py -m output/{scene} --max_hashmap 19'
    print(one_cmd)
    os.system(one_cmd)