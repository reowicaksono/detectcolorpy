import cv2
import numpy as np

from lib.color import detect_colors

# img = cv2.imread(r"C:\Users\Reowi\Music\Dimas Al Basfar_Photo.jpg")
# imgmanipulation = img.copy()
# lower_white = np.array([200, 200, 200])
# upper_white = np.array([255, 255, 255])

# lower_blue = np.array([100, 0, 0])
# upper_blue = np.array([140, 110, 110])

# lower_yellow = np.array([30, 170, 200])
# upper_yellow = np.array([70, 190, 220])

# mask_white = cv2.inRange(imgmanipulation, lower_white, upper_white)
# mask_blue = cv2.inRange(imgmanipulation, lower_blue, upper_blue)
# mask_yellow = cv2.inRange(imgmanipulation,lower_yellow,upper_yellow)

# imgmanipulation[mask_white > 0] = (0, 0, 255)
# imgmanipulation[mask_blue > 0] = (255, 0, 0)
# imgmanipulation[mask_yellow > 0] = (0,255,0)

# imageSizeManipulation = cv2.resize(imgmanipulation, (540, 540)) 
# imageSizeMOriginal = cv2.resize(img, (540, 540)) 
# result_image = detect_colors(imageSizeManipulation)

# cv2.imshow("Original", imageSizeMOriginal)
# cv2.imshow("Result", result_image)
# cv2.waitKey()
# cv2.destroyAllWindows()



input_img = cv2.imread('./assets/test.jpg')
img = cv2.resize(input_img, (640, 480))
# Make a copy to draw contour outline
input_image_cpy = img.copy()

result_image = detect_colors(input_img)
img_manipulate = cv2.resize(result_image, (640, 480))



# Display final output for multiple color detection opencv python
cv2.imshow("Original", img)
cv2.imshow("Result", img_manipulate)
cv2.waitKey()
cv2.destroyAllWindows()