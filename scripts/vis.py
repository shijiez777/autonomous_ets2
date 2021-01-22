import cv2
import numpy as np
import time

data_path = 'D:/data/gta5_data/raw/training_data-0.npy'
data =np.load(data_path, allow_pickle=True)
for im, keys in data:
    cv2.imshow('disp', cv2.cvtColor(im, cv2.COLOR_BGRA2RGB))
    print(keys)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.03)
