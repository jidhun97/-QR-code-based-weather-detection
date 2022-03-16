import cv2
import numpy as np
import pyzbar
from pyzbar.pyzbar import decode

img = cv2.imread('delhi_qr.png')
code = decode(img)


def city():
    for qrcode in code:
        qdata = qrcode.data.decode('utf-8')
        return (qdata)


city()

cityname = city()
