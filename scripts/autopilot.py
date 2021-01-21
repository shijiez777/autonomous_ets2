import os
from timeit import default_timer as timer
import time

fPath = os.path.dirname(os.path.abspath(__file__))
import sys
# ADD project path instead of module path
sys.path.append(os.path.join(fPath, ".."))
from ets2drive.helpers import read_yaml
from ets2drive.classifier import Classifier
from ets2drive.simController import Keyboard

# fps
model_name = '5fps'
model_fps = 10
waitInterval = 1/model_fps

config_path = "../config/config.yml"
config_path = os.path.join(fPath, config_path)
config = read_yaml(os.path.abspath(config_path))
model = Classifier(config)
controller = Keyboard(config)

try:

    while True:
        t1 = timer()
        prob = model.predict()
        print(prob)
        controller.input(prob)
        t2 = timer()
        sleepInterval = max(waitInterval - (t2 - t1), 0)
        # print(t2 - t1)
        # inference time 0.08 sec, roughly 12.5 fps
        time.sleep(sleepInterval)

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass