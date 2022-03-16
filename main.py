from pyzbar.pyzbar import decode
import cv2
from weaterAPI import weather
from weaterAPI import temp1
from QR import cityname
from QR import img

cv2.namedWindow("QR", cv2.WINDOW_KEEPRATIO)

t = str(temp1)
data = cityname+", " + weather+", " + t
cv2.putText(img,data, (500,990),cv2.FONT_HERSHEY_DUPLEX, 1,(0,0,255),2)
cv2.imshow("QR", img)
cv2.waitKey(0)




