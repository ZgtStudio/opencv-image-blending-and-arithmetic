import cv2 # import OpenCV

# read the image
image_1 = cv2.imread("Bison.jpg") 
image_2 = cv2.imread("Falcon.jpg")

# print BGR values at two sample pixel locations
print("First Images BGR Values: ", image_1[100, 100])
print("Second Images BGR Values: ", image_2[150, 120])

# print the summed BGR values (uint8, so result is (a + b) % 256 per channel)
cv2.imshow("Bison", image_1)
cv2.imshow("Falcon", image_2)

print("Summed BGR Values: ", image_1[100, 100]+ image_2[150, 120]) # 

# wait for a key press to destroy all image windows
cv2.waitKey(0)
cv2.destroyAllWindows()