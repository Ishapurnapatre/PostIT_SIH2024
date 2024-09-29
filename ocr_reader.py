# ocr_reader.py
import pytesseract
from PIL import Image

class OCRReader:
    def __init__(self, image_path):
        self.image_path = image_path
    
    def extract_text(self):
        try:
            # Open the image
            image = Image.open(self.image_path)
            # Use pytesseract to extract text
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            print(f"Error in OCR extraction: {e}")
            return None
