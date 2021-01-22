# Done by Frannecklp

import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api

def grab_screen(region=None):

    hwnd = win32gui.FindWindow(None, "Grand Theft Auto V")
    rect = win32gui.GetWindowRect(hwnd)
    w = rect[2] - rect[0]
    h = rect[3] - rect[1]
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h,w,4)

    # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    # hwin = win32gui.GetDesktopWindow()

    # if region:
    #         left,top,x2,y2 = region
    #         width = x2 - left + 1
    #         height = y2 - top + 1
    # else:
    #     width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    #     height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    #     left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    #     top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    # hwindc = win32gui.GetWindowDC(hwin)
    # srcdc = win32ui.CreateDCFromHandle(hwindc)
    # memdc = srcdc.CreateCompatibleDC()
    # bmp = win32ui.CreateBitmap()
    # bmp.CreateCompatibleBitmap(srcdc, width, height)
    # memdc.SelectObject(bmp)
    # memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    
    # signedIntsArray = bmp.GetBitmapBits(True)
    # img = np.fromstring(signedIntsArray, dtype='uint8')
    # img.shape = (height,width,4)

    # srcdc.DeleteDC()
    # memdc.DeleteDC()
    # win32gui.ReleaseDC(hwin, hwindc)
    # win32gui.DeleteObject(bmp.GetHandle())

    return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)


if __name__ == "__main__":
    while 1:
        im = grab_screen()
        cv2.imshow("disp", im)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()