import cv2
import numpy as np
image = cv2.imread('today_image_temp.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
filtered_contours = []
threshold_area=50
for contour in contours:
    area = cv2.contourArea(contour)
    if area > threshold_area:  # Set an appropriate threshold area
        filtered_contours.append(contour)
result_mask = np.zeros_like(thresh)
cv2.drawContours(result_mask, filtered_contours, -1, 255, thickness=cv2.FILLED)
result = cv2.bitwise_and(image, image, mask=result_mask)
print('No. of Bottles:',len(filtered_contours))
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To save the result:
# cv2.imwrite('result_image.jpg', result)
