import cv2 # import OpenCV

image = cv2.imread("Atlantic Puffin.jpg")

cv2.imshow("Atlantic Puffin", image)

cv2.waitKey(0)
cv2.destroyAllWindows()