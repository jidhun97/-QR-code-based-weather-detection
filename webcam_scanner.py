import cv2
import numpy as np
import pyzbar
from pyzbar.pyzbar import decode
import  requests

api_key = '082893c8eb2bf0a0bc66d7a720a040d2'

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
def cityname():
    while True :
        success,img = cap.read()

        code = decode(img)
        for qrcode in code:
            qdata = qrcode.data.decode('utf-8')
            pts = np.array([qrcode.polygon], np.int32)
            cv2.polylines(img, pts, True, (0, 255, 0), 2)
            weather_data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={qdata}&units=metric&APPID={api_key}")
            weather = weather_data.json()['weather'][0]['main']
            temp1 = weather_data.json()['main']['temp']
            rp = qrcode.rect
            t = str(temp1)
            output = qdata +" " +weather+" " +t
            cv2.putText(img,output , (rp[0], rp[1]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)


        cv2.imshow("result", img)
        cv2.waitKey(1)




cityname()

