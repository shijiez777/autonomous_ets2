from PIL import ImageGrab
from win32 import win32gui

hwnd = win32gui.FindWindow(None, r'Euro Truck Simulator 2')
win32gui.SetForegroundWindow(hwnd)
dimensions = win32gui.GetWindowRect(hwnd)
print(dimensions)
dimensions = list(dimensions)
dimensions[0] += 10
dimensions[1] += 30
dimensions[2] -= 10
dimensions[3] -= 10
image = ImageGrab.grab((dimensions))
image.show()