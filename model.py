import numpy as np
import cv2

def detect(frame: np.ndarray) -> np.ndarray:
    # Apply Gaussian blur to reduce noise
    # blurred = cv2.GaussianBlur(frame, (9, 9), 0)
    
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)
    
    # Convert back to BGR format to maintain compatibility
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    return edges_bgr