import requests as req
import json
import time
import csv
import os
import numpy as np

# from PIL import ImageGrab
from datetime import datetime
from timeit import default_timer as timer
import cv2

fPath = os.path.dirname(os.path.abspath(__file__))
import sys
# ADD project path instead of module path
sys.path.append(os.path.join(fPath, ".."))
from ets2drive.helpers import read_yaml
from ets2drive.controllerInput import XboxController
from ets2drive.grabscreen import grab_screen

# time taken requesting json, taking screenshot, saving json and screenshot takes roughly 0.07 sec.
# So it is currently only achieveable with 10 fps.
config_path = "../config/config.yml"
config_path = os.path.join(fPath, config_path)
config = read_yaml(os.path.abspath(config_path))
json_folder = config['json_folder']
img_folder = config['img_folder']

# fps
fps = config['FPS']
waitInterval = 1/fps

data_folder = config['raw_data_folder']
os.makedirs(data_folder, exist_ok=True)
dt = datetime.now()


starting_value = len(os.listdir(data_folder))
file_name = 'training_data-{}.npy'.format(starting_value)




data_timestamp = dt.strftime("%Y-%M-%M_%H_%M_%S")
# img_folder = os.path.join(img_folder, data_timestamp)
# json_folder = os.path.join(json_folder, data_timestamp)
# os.makedirs(json_folder, exist_ok=True)
# os.makedirs(img_folder, exist_ok=True)

xbc = XboxController()

# def screenshot(img_folder, fname):
#     im = ImageGrab.grab()
#     im.save(os.path.join(img_folder, fname))

train_data = []


for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

try:
    while True:
        t1 = timer()
        # response = req.get("http://localhost:25555/api/ets2/telemetry")
        # raw_data = json.loads(response.content)
        # im = ImageGrab.grab()

        # dt = datetime.now()
        # fileName = "{}.{}".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000)

        # fname = fileName + config['img_ext']

        # im.save(os.path.join(img_folder, fname))
        
        # add controller state to json
        # raw_data['uinput'] = xbc.read()
        # print(raw_data['uinput'])
        # with open(os.path.join(json_folder, (fileName +'.json')), 'w') as outfile:
        #     json.dump(raw_data, outfile)
        im = grab_screen()
        im = cv2.resize(im, (480, 270))
        keys = xbc.read()
        # cv2.imshow('disp', im)
        # print(keys)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        train_data.append([im, keys])
        if len(train_data) == 1000:
            np.save(os.path.join(data_folder, file_name), train_data)
            train_data = []
            starting_value = len(os.listdir(data_folder))
            file_name = 'training_data-{}.npy'.format(starting_value)
            print("saved: " + str(time.time()))
        t2 = timer()
        # print(str(t2 - t1), end = '\r')
        time.sleep(max(waitInterval - (t2 - t1), 0))

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    
    cv2.destroyAllWindows()

    pass