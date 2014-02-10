# Sources visited that work: 
# http://stackoverflow.com/questions/18721552/opencv2-python-createbackgroundsubtractor-module-not-found
# http://stackoverflow.com/questions/14554946/opencv-python-mask-in-module-cv2-while-streaming-webcam-video

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow('camshift')

# fgbg = cv2.BackgroundSubtractorMOG2()

fgbg = cv2.BackgroundSubtractorMOG()

print fgbg

while(True):
	ret, frame = cap.read()
	print ret

	if ret:
	
		fgmask = fgbg.apply(frame)

		cv2.imshow('frame', fgmask)

		# print fgmask

	k = cv2.waitKey(1) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()