# Sources visited that worked
# http://stackoverflow.com/questions/18835941/unable-to-write-video-using-python-and-opencv2-on-mac-os-x

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow('camshift')

'''
This file records and saves (in .avi format) video in gray scale

'''

# # Define the codec and create VideoWriter object
fourcc = cv2.cv.FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi', -1, 25, (640,480), 1)

print fourcc
print out


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if (ret):
    	# Set screen size - if uncomment, won't be able to save video
    	# cap.set(3, 1280)
        # cap.set(4, 720)

        # write the frame
        out.write(frame)
	    # Our operations on the frame come here
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    	# Display the resulting frame in gray. For color, pass frame as second parameter
    	cv2.imshow('my window', gray)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
