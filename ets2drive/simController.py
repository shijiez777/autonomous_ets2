import pydirectinput
import numpy as np

class Keyboard:
    def __init__(self, config):
        self.labels = config['label_columns']
        self.keys = np.array(config['keys'])
        self.clfThreshold = config['clfThreshold']
        self.previousKeys = set()

    def input(self, probs):
        flags = probs[0] > self.clfThreshold
        keys = set(self.keys[flags])
        # ups = self.previousKeys.difference(keys)
        # downs = keys.difference(self.previousKeys)
        # print("up:")
        # print(ups)
        # print("down:")
        # print(downs)
        print(keys)
        for k in self.previousKeys.difference(keys):
            pydirectinput.keyUp(k)
        for k in keys.difference(self.previousKeys):
            pydirectinput.keyDown(k)
        self.previousKeys = keys




if __name__ == '__main__':
    prevKeys = set()
    keys = [set((1, 2, 3)), set([2, 3]), set([1]), set([1, 2])]
    while keys:
        key = keys.pop(0)
        ups = prevKeys.difference(key)
        downs = key.difference(prevKeys)
        print(ups)
        print(downs)
        print('-'*20)
        prevKeys = key