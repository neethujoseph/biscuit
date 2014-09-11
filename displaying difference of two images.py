#importing modules
import numpy		
import cv2			

#capturing video
cap = cv2.VideoCapture(0)
#reading frame
gray_1 = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
	
while(True):
	gray_2 = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
	#calculating difference
	difference=cv2.absdiff(gray_2,gray_1)
	#calculating mean
	numpy.mean(difference)
	gray_1=gray_2
	gray_2=cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
	#displaying difference
	cv2.imshow('difference',difference)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# When everything done, release the capture
cap.release()

# Close everything.
cv2.destroyAllWindows()
