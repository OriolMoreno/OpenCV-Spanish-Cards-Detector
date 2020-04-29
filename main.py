import cv2
import matplotlib.pyplot as plt
import numberDetection
import cardDetection
import cardProcessing
import numpy as np
import imutils
from imutils import contours

img = cv2.imread("test/cardBlackBackground.jpg")

plt.imshow(img)
plt.show()

img = cardProcessing.downscale(img)

cardContours, cardCorners = cardDetection.detectCards(img)

cardsFound = cardDetection.extractCards(img, cardContours, cardCorners)

for cardFound in cardsFound:

    cropCard = cardFound[10:40, 10:40]

    numberDetection.detectNumbers(cropCard)

