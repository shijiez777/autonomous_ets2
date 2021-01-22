# https://github.com/kevinhughes27/TensorKart/blob/master/utils.py
import math
from inputs import get_gamepad
import threading
import time

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8) # 256
    MAX_JOY_VAL = math.pow(2, 15) # 32768

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0
        self.stateDict = {'steer': 0, 'throttle': 0, 'brake': 0}

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self):
        # self.stateDict['steer'] = self.LeftJoystickX
        # self.stateDict['throttle'] = self.RightTrigger
        # self.stateDict['brake'] = self.LeftTrigger
        # x = self.LeftJoystickX
        # y = self.LeftJoystickY
        # a = self.A
        # b = self.X # b=1, x=2
        # rb = self.RightBumper
        
        # return self.stateDict
        return [self.LeftJoystickX, self.RightTrigger, self.LeftTrigger]

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                    #if self.LeftJoystickY > 0.1 or self.LeftJoystickY < -0.1:
                    #    print(self.LeftJoystickY)
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                    #if self.LeftJoystickX > 0.1 or self.LeftJoystickX < -0.1:
                    #    print(self.LeftJoystickX)
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                    #if self.RightJoystickY > 0.1 or self.RightJoystickY < -0.1:
                    #    print(self.RightJoystickY)
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                    #if self.RightJoystickX > 0.1 or self.RightJoystickX < -0.1:
                        #print(self.RightJoystickX)
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                    #print(self.LeftTrigger)
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                    #print(self.RightTrigger)
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                    #print(self.LeftBumper)
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                    #print(self.RightBumper)
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                    #print(self.A)
                elif event.code == 'BTN_NORTH':
                    self.X = event.state
                    #print(self.X)
                elif event.code == 'BTN_WEST':
                    self.Y = event.state
                    #print(self.Y)
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                    #print(self.B)
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                    #print(self.LeftThumb)
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                    #print(self.RightThumb)
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                    #print(self.Back)
                elif event.code == 'BTN_START':
                    self.Start = event.state
                    #print(self.Start)
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                    #print(self.LeftDPad)
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                    #print(self.RightDPad)
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                    # print(self.UpDPad)
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state
                    # print(self.DownDPad)


if __name__ == '__main__':
    c = XboxController()
    # c. _monitor_controller()
    while 1:
        print(c.read())
        time.sleep(0.1)