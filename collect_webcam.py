import cv2
import os

import urllib
import numpy as np
import cv2
import os

# for file_type in ['negativas', 'positivas']:
#     for img in os.listdir(file_type):
#         if file_type == 'negativas':
#             line = file_type + '/' + img + '\n'

#             with open('bg.txt', 'a') as f:
#                 f.write(line)

#         elif file_type == 'positivas':
#             line = file_type + '/' + img + ' 1 0 0 150 150\n'

#             with open('info.dat', 'a') as f:
#                 f.write(line)

import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    frame
