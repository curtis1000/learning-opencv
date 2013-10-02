import cv2

cameraCapture = cv2.VideoCapture(0)

if not cameraCapture:
     print "Failed to initialize capture"

fps = 30 # assumption

size = (int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

print size

videoWriter = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('I','4','2','0'), fps, size)

success, frame = cameraCapture.read()
print success

numFramesRemaining = 10 * fps - 1

while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1