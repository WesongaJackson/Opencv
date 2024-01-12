import  cv2
img=cv2.imread("footer.png")
cv2.imwrite("new_logo.jpg",img)
cv2.imshow("PS LOGO",img)
cv2.waitKey(0)
cv2.destroyAllWindows()