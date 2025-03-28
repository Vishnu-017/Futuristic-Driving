import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils

# Read the image
img = cv2.imread('D:\\Python\\mini project\\final\\image3.jpg')
if img is None:
    print("Error: Could not load image")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(1)
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
plt.title('Grayscale Image')

# Apply bilateral filter for noise reduction
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
# Edge detection using Canny
edged = cv2.Canny(bfilter, 30, 200)
plt.figure(2)
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
plt.title('Edge Detection')

# Find contours
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# Find rectangular contour
location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

print("Contour coordinates:", location)

# Create mask and apply it
if location is not None:
    mask = np.zeros(gray.shape, dtype=np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)
    
    plt.figure(3)
    plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    plt.title('Masked Image')

    # Get bounding box coordinates
    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))

    # Crop the image
    cropped_image = gray[x1:x2+1, y1:y2+1]
    plt.figure(4)
    plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
    plt.title('Cropped Image')

    # Save the result
    success = cv2.imwrite("detections.jpg", cropped_image)
    if success:
        print("Image successfully saved as detections.jpg")
    else:
        print("Error saving image")
else:
    print("No rectangular contour found")

plt.show()
