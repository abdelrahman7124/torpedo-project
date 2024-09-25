import cv2
import numpy as np

def process_frame(frame):
    # Step 1: Convert to grayscale and blur
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    _, threshold_frame = cv2.threshold(blurred_frame, 50, 255, cv2.THRESH_BINARY_INV)

    # Step 2: Detect contours
    contours, _ = cv2.findContours(threshold_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours if detected
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(frame, [largest_contour], -1, (0, 0, 255), 2)

    # Step 3: Detect lines
    canny_frame = cv2.Canny(blurred_frame, 50, 150)
    lines = cv2.HoughLinesP(canny_frame, 1, np.pi / 180, threshold=100, minLineLength=30, maxLineGap=10)
    
    # Draw lines if detected
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # Step 4: Control logic based on contours and lines
    control_signal = control_robot(contours, lines, frame.shape[1])

    # Return the processed frame and control signal
    return frame, control_signal 

def control_robot(contours, lines, width):
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M['m00'] > 0:
            cx = int(M['m10'] / M['m00'])
            avg_position = cx
        else:
            return "Stop"
    else:
        return "Stop"

    if lines is not None:
        line_positions = [(x1 + x2) // 2 for x1, y1, x2, y2 in lines[:, 0]]
        avg_line_position = np.mean(line_positions)
        avg_position = (avg_position + avg_line_position) // 2

    if avg_position < width // 3:
        return "Turn Left"
    elif avg_position > 2 * width // 3:
        return "Turn Right"
    else:
        return "Move Forward"