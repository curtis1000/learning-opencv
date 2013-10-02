import cv2

videoCapture = cv2.VideoCapture('sample.avi')
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)

size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

# uncompressed YUV encoding
videoWriter = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('I','4','2','0'), fps, size)

# MPEG-1
# videoWriter = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('P','I','M','1'), fps, size)

# motion-JPEG
#videoWriter = cv2.VideoWriter('output.avi', cv2.cv.CV_FOURCC('M','J','P','G'), fps, size)

# Ogg-Vorbis
#videoWriter = cv2.VideoWriter('output.ogv', cv2.cv.CV_FOURCC('T','H','E','O'), fps, size)

# Flash Video
# videoWriter = cv2.VideoWriter('output.flv', cv2.cv.CV_FOURCC('F','L','V','1'), fps, size)
                              
success, frame = videoCapture.read()

while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()