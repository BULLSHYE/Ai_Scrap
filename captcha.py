# # import cv2
# # import numpy as np

# # # Load the image
# # image = cv2.imread("AI-Web-Scraper-main/image.png")

# # # Convert to grayscale
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # # Apply adaptive thresholding to enhance contrast
# # thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
# #                                cv2.THRESH_BINARY, 11, 2)

# # # Apply morphological operations to remove noise
# # kernel = np.ones((2, 2), np.uint8)
# # morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

# # # Apply Canny edge detection (optional)
# # edges = cv2.Canny(morph, 50, 150)

# # # Display the results
# # cv2.imshow("Original", image)
# # cv2.imshow("Grayscale", gray)
# # cv2.imshow("Thresholded", thresh)
# # cv2.imshow("Morphological Transform", morph)
# # cv2.imshow("Edges", edges)

# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# import cv2
# import numpy as np
# import easyocr

# # Load the CAPTCHA image
# image = cv2.imread("AI-Web-Scraper-main/image.png")

# # Convert to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply bilateral filter to remove noise while keeping edges sharp
# filtered = cv2.bilateralFilter(gray, 9, 75, 75)

# # Apply adaptive thresholding for better contrast
# thresh = cv2.adaptiveThreshold(filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                cv2.THRESH_BINARY_INV, 11, 2)

# # Morphological operations to clean the image
# kernel = np.ones((2, 2), np.uint8)
# processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)

# # Apply dilation to enhance character edges
# processed = cv2.dilate(processed, kernel, iterations=1)

# # Initialize EasyOCR reader (English + Numbers)
# reader = easyocr.Reader(['en'])

# # Read text from CAPTCHA
# result = reader.readtext(processed, detail=0)

# # Extract detected text and ensure uppercase formatting
# captcha_text = "".join(result).upper()

# # Show processed image (for debugging)
# cv2.imshow("Original CAPTCHA", image)
# cv2.imshow("Processed CAPTCHA", processed)
# print("Extracted CAPTCHA Text:", captcha_text)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Print extracted CAPTCHA text
# https://github.com/2captcha/2captcha-python

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

try:
    result = solver.recaptcha(
        sitekey='6LfD3PIbAAAAAJs_eEHvoOl75_83eXSqpPSRFJ_u',
        url='https://2captcha.com/demo/recaptcha-v2')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))