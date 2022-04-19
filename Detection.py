from math import ceil
import sys
import cv2
import numpy as np
  
# Read the images
img = cv2.imread("Rgb.jpg")
  
# Resizing the image
image = cv2.resize(img, (660, 660))

# Convert Image to Image HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV values RED
lower_Red   = np.array([0, 100, 100])
upper_Red   = np.array([55, 255, 255])

# HSV values GREEN
lower_Green = np.array([50, 100, 100])
upper_Green = np.array([70, 255, 255])

# HSV values BLUE
lower_Blue  = np.array([100, 100, 100])
upper_Blue  = np.array([140, 255, 255])

Red    = cv2.inRange(hsv, lower_Red, upper_Red)
Green  = cv2.inRange(hsv, lower_Green, upper_Green)
Blue   = cv2.inRange(hsv, lower_Blue, upper_Blue)

print("\n\n---------------- PX POR COR ----------------")

pixelsRed   = cv2.countNonZero(Red)
pixelsGreen = cv2.countNonZero(Green)
pixelsBlue  = cv2.countNonZero(Blue)
totalcv2    = pixelsRed + pixelsGreen + pixelsBlue

print('RED      | Px: ', pixelsRed)
print('GREEN    | Px: ', pixelsGreen)
print('BLUE     | Px: ', pixelsBlue)
print('Total Px | Px: ', totalcv2)

print('----------- PORCENTAGEM POR COR -----------')

print('RED      | {}%: ' .format(ceil((pixelsRed  /totalcv2)*100)))
print('GREEN    | {}%: ' .format(ceil((pixelsGreen/totalcv2)*100)))
print('BLUE     | {}%: ' .format(ceil((pixelsBlue /totalcv2)*100)))

# Display Image and Mask
cv2.imshow("Image", image)
cv2.imshow("Red",   Red)
cv2.imshow("Green", Green)
cv2.imshow("Blue",  Blue)
  
# Make python sleep for unlimited time
cv2.waitKey(0)