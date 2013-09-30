import cv2
import numpy
import os

# make an array of 120,000 random bytes
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

# convert the array to make a 400x300 grayscale image
grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png', grayImage)

# convert the array to make a 400x100 color image
bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('RandomColor.png', bgrImage)