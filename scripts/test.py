import requests as req
import time
import json
from PIL import ImageGrab


while 1:
    t1 = time.time()
    # response = req.get("http://localhost:25555/api/ets2/telemetry")
    # raw_data = json.loads(response.content)
    im = ImageGrab.grab()

    
    t2 = time.time()
    print(t2 - t1)