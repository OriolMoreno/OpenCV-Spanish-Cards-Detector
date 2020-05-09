import cv2
import matplotlib.pyplot as plt
import cardDetection
import cardProcessing
import numberDetection
import suitDetection
import numpy as np
import imutils
from imutils import contours

#img = cv2.imread("test/cardsBriscaMode.jpg")
img = cv2.imread("test/cardBlackBackground.jpg")

plt.imshow(img)
plt.show()

img = cardProcessing.downscale(img)

cardContours, cardCorners = cardDetection.detectCards(img)

cardsFound = cardDetection.extractCards(img, cardContours, cardCorners)

for cardFound in cardsFound:

    cropCard = cardFound[12:35, 12:35]
    number = numberDetection.detectNumbers(cropCard)
    cropCard2 = cardFound[10:22, :]
    suit = suitDetection.findSuit(cropCard2)

    print("Number: ", number, " Suit: ", suit)

