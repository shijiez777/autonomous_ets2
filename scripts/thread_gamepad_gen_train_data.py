import requests as req
import json
import time
import csv
import os

from PIL import ImageGrab
from datetime import datetime
from timeit import default_timer as timer

fPath = os.path.dirname(os.path.abspath(__file__))
import sys
# ADD project path instead of module path
sys.path.append(os.path.join(fPath, ".."))
from ets2drive.helpers import read_yaml
from ets2drive.controllerInput import XboxController
import threading

#### NO improvement in terms of fps compared to single thread 10 FPS max.

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

dt = datetime.now()
data_timestamp = dt.strftime("%Y-%M-%M_%H_%M_%S")
img_folder = os.path.join(img_folder, data_timestamp)
json_folder = os.path.join(json_folder, data_timestamp)
os.makedirs(json_folder, exist_ok=True)
os.makedirs(img_folder, exist_ok=True)

xbc = XboxController()

def screenshot(img_folder, fname):
    im = ImageGrab.grab()
    im.save(os.path.join(img_folder, fname))

def read_game_state_and_save(sim_conrtoller,json_folder, file_name):
    response = req.get("http://localhost:25555/api/ets2/telemetry")
    raw_data = json.loads(response.content)
    # add controller state to json
    raw_data['uinput'] = sim_conrtoller.read()
    # print(raw_data['uinput'])
    with open(os.path.join(json_folder, (file_name +'.json')), 'w') as outfile:
        json.dump(raw_data, outfile)

try:
    while True:
        t1 = timer()
        dt = datetime.now()
        json_filename = "{}.{}".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000)
        img_fname = json_filename + config['img_ext']
        # thread to take screenshot
        sc_thread = threading.Thread(target=screenshot, args=(img_folder, img_fname))
        sc_thread.daemon = True
        sc_thread.start()

        data_thread = threading.Thread(target=read_game_state_and_save, args=(xbc, json_folder, json_filename))
        data_thread.daemon = True
        data_thread.start()
        # sc_thread.join()
        # data_thread.join()
        t2 = timer()
        # print(t2 - t1)
        # print(waitInterval - (t2 - t1))
        time.sleep(max(waitInterval - (t2 - t1), 0))

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass

"""
threaded, not waiting, 20 fps 0.05sec 89 items
single thread, 20 fps, 89/90

10 fps
threaded not waiting, 79
single thread 80
"""