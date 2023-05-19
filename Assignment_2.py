import cv2
import numpy as np
import os

def pixel(p):
   if p > 100:
        return 255
   else:
        return int((205*p+5000)/100)

kernel = np.array([[1, 1, 1], [1, 9, 1], [1, 1, 1]]) / 17

cap = cv2.VideoCapture(r"C:\Users\Lenovo\Desktop\Assignment 2 Media\noisyvideo2.mp4")
if not cap.isOpened():
    exit("Error")

os.makedirs('AvgFilter ImgSeg', exist_ok=True)
os.makedirs('PixelTransform_ImgSeq', exist_ok=True)

for c in range(10):
    ret, frame = cap.read()
    if not ret:
        break
    fframe = cv2.filter2D(frame, -1, kernel)
    tframe = np.vectorize(pixel)(fframe)
    cv2.imwrite(f'AvgFilter ImgSeg/filtered_{c}.jpg', fframe)
    cv2.imwrite(f'PixelTransform_ImgSeq/transformed_{c}.jpg', tframe)
    
cap.release()
cv2.destroyAllWindows()


