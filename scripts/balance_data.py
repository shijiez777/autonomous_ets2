import cv2
import numpy as np
import time
import os

fPath = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(os.path.join(fPath, ".."))
from ets2drive.helpers import read_yaml
config_path = "../config/config.yml"
config_path = os.path.join(fPath, config_path)
config = read_yaml(os.path.abspath(config_path))

raw_data_folder = config['raw_data_folder']
balanced_data_folder = config['balanced_data_folder']
os.makedirs(balanced_data_folder, exist_ok=True)

b = 0
l = 0
r = 0
a = 0
free = 0
for raw_fname in os.listdir(raw_data_folder):
    data =np.load(os.path.join(raw_data_folder, raw_fname), allow_pickle=True)
    for im, keys in data:
        if keys[2]:
            b += 1
        elif keys[0] < -0.05:
            l += 1
        elif keys[0] > 0.05:
            r += 1
        elif keys[1] > 0:
            a += 1
        else:
            # print(keys)
            free += 1
print('brake: ' + str(b))
print('left: ' + str(l))
print('right: ' + str(r))
print('accelerate: ' + str(a))
print('no buttonpress: ' + str(free))