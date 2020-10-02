import cv2
import numpy as np

img = cv2.imread('book .jpg')

width, height = 250, 350
# img.resize = cv2.resize(img, (width, height))
pts1 = np.float32([[92, 135], [136, 44], [209, 207], [266, 98]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
print(pts1)
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

for x in range(0, 4):
    cv2.circle(img, (pts1[x][0], pts1[x][1]), 3, (57, 225, 20), cv2.FILLED)

cv2.imshow('Original image', img)
cv2.imshow('Output Image', imgOutput)
cv2. waitKey(0)
cv2.destroyAllWindows()