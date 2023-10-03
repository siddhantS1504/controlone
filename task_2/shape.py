import cv2
import numpy as np

# Create a black image
image = np.zeros((700, 500, 3), dtype=np.uint8)

# Initial Y-coordinate
y_coordinate = 50

# Draw a line
cv2.line(image, (50, y_coordinate), (450, y_coordinate), (0, 255, 0), 2)
y_coordinate += 50

# Draw a rectangle
cv2.rectangle(image, (50, y_coordinate), (450, y_coordinate + 100), (0, 0, 255), 2)
y_coordinate += 120

# Draw a filled rectangle
cv2.rectangle(image, (50, y_coordinate), (450, y_coordinate + 100), (255, 0, 0), -1)
y_coordinate += 120

# Draw an ellipse
cv2.ellipse(image, (250, y_coordinate + 50), (100, 50), 0, 0, 360, (255, 255, 0), 2)
y_coordinate += 120

# Draw a filled circle
cv2.circle(image, (250, y_coordinate + 50), 30, (0, 255, 255), -1)

# Display the image
cv2.imshow('Geometric Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
