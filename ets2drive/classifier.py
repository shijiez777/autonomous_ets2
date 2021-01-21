import os
from PIL import ImageGrab
import tensorflow as tf
import numpy as np
from PIL import ImageGrab
from win32 import win32gui

# allow gpu to run
import tensorflow as tf
config = tf.compat.v1.ConfigProto(gpu_options = 
                         tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8)
# device_count = {'GPU': 1}
)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)


class Classifier:
    def __init__(self, config):
        self.clfThreshold = config['clfThreshold']
        self.resize_dim = [config['resize_H'], config['resize_W']]
        self.model = tf.keras.models.load_model(os.path.join(config['model_folder'], config['model_name']))
        self.dimensions = None 

    def screenshot(self):
        if not self.dimensions:
            hwnd = win32gui.FindWindow(None, r'Euro Truck Simulator 2')
            win32gui.SetForegroundWindow(hwnd)
            dimensions = win32gui.GetWindowRect(hwnd)
            dimensions = list(dimensions)
            dimensions[0] += 10
            dimensions[1] += 30
            dimensions[2] -= 10
            dimensions[3] -= 10
            self.dimensions = (dimensions)
        return ImageGrab.grab(bbox =self.dimensions) 
    
    def preprocess(self, im):
        im = tf.keras.preprocessing.image.img_to_array(im, dtype=np.float64)
        im = tf.convert_to_tensor(im)
        im = tf.image.resize(im, self.resize_dim)
        im = tf.expand_dims(im, 0)
        return im

    def predict(self):
        im = self.screenshot()
        im = self.preprocess(im)
        prob = self.model.predict(im)
        return prob

if __name__ == "__main__":
    fPath = os.path.dirname(os.path.abspath(__file__))
    import sys
    sys.path.append(os.path.join(fPath, ".."))
    from ets2drive.helpers import read_yaml

    config_path = "../config/config.yml"
    config_path = os.path.join(fPath, config_path)
    config = read_yaml(os.path.abspath(config_path))
    model = Classifier(config)
    prob = model.predict()
    print(prob)