import cv2

cameraCapture = cv2.VideoCapture(1)

if not cameraCapture:
     print "Failed to initialize capture"

fps = 30 # assumption

size = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

print size

# works on my win 7 laptop for encoding to a playable file
videoWriter = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('i','Y', 'U', 'V'), fps, size)

# MPEG-1
#videoWriter = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('P','I','M','1'), fps, size)

# motion-JPEG
#videoWriter = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('M','J','P','G'), fps, size)

# Ogg-Vorbis
#videoWriter = cv2.VideoWriter('output.ogv', cv2.cv.CV_FOURCC('T','H','E','O'), fps, size)

# Flash Video
#videoWriter = cv2.VideoWriter('output.flv', cv2.cv.CV_FOURCC('F','L','V','1'), fps, size)

success, frame = cameraCapture.read()
print success

numFramesRemaining = 10 * fps - 1

while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1