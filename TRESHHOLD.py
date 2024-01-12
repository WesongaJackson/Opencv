import cv2

img = cv2.imread("footer.png")
grayImage = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
thresImg = cv2.threshold(grayImage, 220, 255, cv2.THRESH_BINARY)[1]


cv2.imwrite("TreshImages6.jpg", thresImg)
cv2.imshow("ThreshImage",thresImg)
cv2.waitKey(0)
cv2.destroyAllWindows()