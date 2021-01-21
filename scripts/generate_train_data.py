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


# fps
fps = 10
waitInterval = 1/fps

# time taken requesting json, taking screenshot, saving json and screenshot takes roughly 0.07 sec.
# So it is currently only achieveable with 10 fps.

config_path = "../config/config.yml"

config_path = os.path.join(fPath, config_path)

config = read_yaml(os.path.abspath(config_path))
json_folder = config['json_folder']
img_folder = config['img_folder']

dt = datetime.now()
data_timestamp = dt.strftime("%Y-%M-%M_%H_%M_%S")

img_folder = os.path.join(img_folder, data_timestamp)
json_folder = os.path.join(json_folder, data_timestamp)

os.makedirs(json_folder, exist_ok=True)
os.makedirs(img_folder, exist_ok=True)

try:

    while True:
        t1 = timer()
        response = req.get("http://localhost:25555/api/ets2/telemetry")
        raw_data = json.loads(response.content)
        im = ImageGrab.grab()

        dt = datetime.now()
        fileName = "{}.{}".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000)

        fname = fileName + config['img_ext']

        im.save(os.path.join(img_folder, fname))
        
        with open(os.path.join(json_folder, (fileName +'.json')), 'w') as outfile:
            json.dump(raw_data, outfile)
        t2 = timer()
        # print(waitInterval - (t2 - t1))

        time.sleep(max(waitInterval - (t2 - t1), 0))

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass