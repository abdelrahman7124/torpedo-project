import cv2
import numpy as np

def process_shape_detection(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray, (9, 9), 0)
    median = cv2.medianBlur(gaussian, 9)
    canny = cv2.Canny(median, 50, 150)

    kernel = np.ones((9, 9), np.uint8)
    closed = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

    # Dilate the edges
    kernel = np.ones((1, 1), np.uint8)
    dilated = cv2.dilate(closed, kernel, iterations=1)

    # Find contours
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Filter contours based on area and shape
    filtered_contours = []
    detected_boxes = []
    detected_shapes = []
    detected_colors = []
    min_area = 100

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_area:
            shape = detect_shape(contour)

            if shape in ["triangle", "sq", "circle"]:
                bounding_box = cv2.boundingRect(contour)
                
                # Check for overlap with already detected contours
                is_duplicate = False
                for detected_box in detected_boxes:
                    if boxes_overlap(bounding_box, detected_box):
                        is_duplicate = True
                        break

                # If no overlap, consider it as a new object
                if not is_duplicate:
                    filtered_contours.append(contour)
                    detected_boxes.append(bounding_box)

                    # Detect color inside the shape
                    color = detect_color_inside_shape(frame, contour)
                    
                    # Append detected shape and color to separate lists
                    detected_shapes.append(shape)
                    detected_colors.append(color)

    # Draw filtered contours on the original image
    for contour, shape in zip(filtered_contours, detected_shapes):
        contour_color = (0, 0, 255) if shape == "triangle" else (0, 255, 0) if shape == "sq" else (255, 0, 0)
        cv2.drawContours(frame, [contour], -1, contour_color, 3)

    # Return the frame, separate lists of shapes and colors, and count of detected shapes
    return frame, len(filtered_contours), detected_shapes, detected_colors

def detect_shape(contour):
    # Simplified shape detection logic
    approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    if len(approx) == 3:
        return "triangle"
    elif len(approx) == 4:
        return "sq"
    elif len(approx) > 4:
        return "circle"
    return "unknown"

def detect_color_inside_shape(frame, contour):
    # Create a mask for the shape
    mask = np.zeros_like(frame)
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)

    # Mask the frame and compute the mean color within the shape
    mean_color = cv2.mean(frame, mask=cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY))[:3]  # Get the RGB values

    # Convert the mean color to a more readable format (approximate color name)
    return get_color_name(mean_color)

def get_color_name(mean_color):
    # Unpack the BGR color values
    blue, green, red = mean_color
    
    # Check for color ranges based on BGR values
    if blue > 150 and green < 100 and red < 100:
        return "Blue"
    elif green > 150 and blue < 100 and red < 100:
        return "Yellow"
    elif red > 150 and green < 100 and blue < 100:
        return "Red"
    elif blue < 100 and green > 150 and red > 150:
        return "Green"
    elif blue > 200 and green > 200 and red > 200:
        return "White"
    elif blue < 50 and green < 50 and red < 50:
        return "Black"
    else:
        return "Unknown"


def boxes_overlap(box1, box2):
    # Check if two bounding boxes overlap
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2
    return not (x1 > x2 + w2 or x1 + w1 < x2 or y1 > y2 + h2 or y1 + h1 < y2)
