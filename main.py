import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	img = cv2.medianBlur(gray_img, 5)
	cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

	circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1=5, param2=38, minRadius=0, maxRadius=30)

	if circles is not None:
		circles = np.uint16(np.around(circles))

		for i in circles[0, :]:
			#	draw	the	outer	circle
			cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 6)
			#	draw	the	center	of	the	circle
			cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)


	cv2.imshow("Frame", frame)
	if cv2.waitKey(100) == ord('q'):
		break



cap.release()
cv2.destroyAllWindows()

'''
	pts1 = np.float32([[140, 80],[450, 80],[140, 340],[450, 340]])
	pts2 = np.float32([[0,0], [400, 0], [0, 300], [400, 300]])
	matrix = cv2.getPerspectiveTransform(pts1, pts2)

	frame = cv2.warpPerspective(frame, matrix, (450, 350))
'''