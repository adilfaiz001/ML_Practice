import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")
cv2.imshow("Canvas",canvas)

green = (0,255,0)
cv2.line(canvas,(0,0),(150,150),(255,255,255),15)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)