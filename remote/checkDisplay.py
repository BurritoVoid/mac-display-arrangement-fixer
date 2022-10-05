from picamera2 import Picamera2, Preview
import time
import cv2
import numpy as np

picam2 = Picamera2()
picam2.start()
time.sleep(2)

img = np.empty((480, 640, 3))
img = picam2.capture_array()

# Swap Red and Blue color channels to correct image
corrected_image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Preview of what the camera saw
# cv2.imwrite('whatisee.png',corrected_image)

# Convert Image to Image HSV
hsv = cv2.cvtColor(corrected_image, cv2.COLOR_BGR2HSV)
  
# Defining lower and upper bound HSV values - range of color to accept
lower = np.array([100, 100, 100])
upper = np.array([140, 255, 255])
  
# Defining mask for detecting color - return only pixels in this range
mask = cv2.inRange(hsv, lower, upper)
# cv2.imwrite('./mask.png',mask)

# Slice to check
evalslice = mask[370:470, 500:600]
# cv2.imwrite('./eval.png',evalslice)

# If the mask slice is entirely white, it was the blue square
if np.mean(evalslice) == 255:
    print("FOUND")
else:
    print("NOT FOUND")