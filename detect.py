from paddleocr import PaddleOCR
import cv2
import numpy as np

# Initialize PaddleOCR
ocr = PaddleOCR(lang='en', use_angle_cls=True)

def vech_no(image_path='detections.jpg'):
    """
    Extract vehicle number from an image using OCR
    Returns: string containing the detected vehicle number
    """
    try:
        # Read image
        image_cv = cv2.imread(image_path)
        if image_cv is None:
            raise ValueError(f"Could not load image at {image_path}")

        # Get image dimensions
        image_height, image_width = image_cv.shape[:2]
        print(f"Image dimensions: {image_width}x{image_height}")

        # Perform OCR
        output = ocr.ocr(image_path)
        if not output or not output[0]:
            raise ValueError("No text detected in image")

        # Process OCR results
        # output is a list of lists, where each inner list contains detection results
        results = output[0]  # Get first page of results
        
        # Extract text from first detection
        for result in results:
            box = result[0]  # Coordinates
            text_info = result[1]  # (text, confidence)
            number = text_info[0]
            confidence = text_info[1]
            
            print(f"Detected text: {number} (Confidence: {confidence:.2f})")
            
            # Optionally visualize results
            image_boxes = image_cv.copy()
            pt1 = (int(box[0][0]), int(box[0][1]))  # Top-left corner
            pt2 = (int(box[2][0]), int(box[2][1]))  # Bottom-right corner
            
            # Draw rectangle and text
            cv2.rectangle(image_boxes, pt1, pt2, (0, 0, 255), 1)
            cv2.putText(image_boxes, number, pt1, 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (222, 0, 0), 2)
            
            # Save visualization
            cv2.imwrite('displaying.jpg', image_boxes)
            
            return number  # Return first detected number

        raise ValueError("No valid vehicle number found")

    except Exception as e:
        print(f"Error in vehicle number detection: {str(e)}")
        return None

if __name__ == "__main__":
    # Test the function
    number = vech_no()
    if number:
        print(f"Final vehicle number: {number}")
    else:
        print("Failed to detect vehicle number")
