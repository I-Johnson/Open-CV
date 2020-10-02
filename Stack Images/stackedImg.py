import cv2
import numpy as np
kernel = np.ones((5, 5), np.uint8)

path = "resources/lena.jpg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7, 7), 0)
imgCanny = cv2.Canny(imgBlur, 100, 100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErosion = cv2.erode(imgDilation, kernel, iterations=1)
hstack = np.hstack([imgErosion, imgDilation, imgCanny])
vstack = np.vstack([imgGray, imgBlur])
# stack = np.vstack([hstack, vstack])
# cv2.imshow = ('Combined', stack)
cv2.imshow('Horizontal Stacking', hstack)
cv2.imshow('Vertical stacking', vstack)

# cv2.imshow('img', img)
# cv2.imshow('imgGray', imgGray)
# cv2.imshow('imgBlur', imgBlur)
# cv2.imshow('imgCanny', imgCanny)
# cv2.imshow('imgDilation', imgDilation)
# cv2.imshow('imgErosion', imgErosion)

cv2.waitKey(0)