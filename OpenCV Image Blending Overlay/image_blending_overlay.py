import cv2  # import OpenCV

# read the images from disk
image_1 = cv2.imread("Horse.jpg")
image_2 = cv2.imread("Swan.jpg")

# display the original images in separate windows
cv2.imshow("Horse", image_1)
cv2.imshow("Swan", image_2)

# simple pixel-wise addition of the two images (uint8 wrap-around)
overlay = cv2.add(image_1, image_2)

# weighted image blending (0.7 * image_1 + 0.3 * image_2)
weighted_overlay = cv2.addWeighted(image_1, 0.7, image_2, 0.3, 0)

# display the results: simple addition vs weighted blending
cv2.imshow("Overlay (cv2.add)", overlay)
cv2.imshow("Weighted Overlay", weighted_overlay)

# wait for a key press, then close all image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
