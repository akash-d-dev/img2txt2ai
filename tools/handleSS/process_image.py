from PIL import ImageGrab
import os
import time
import uuid
import pytesseract
from PIL import Image


class Screenshot:
    def process_image():
        image = ImageGrab.grabclipboard()
        filename = None

        if not os.path.exists("temp"):
            os.makedirs("temp")

        if isinstance(image, Image.Image):
            filename = f"{int(time.time())}_{str(uuid.uuid4())[:8]}.png"
            image.save(f"temp/{filename}")
            print(f"Screenshot saved as {filename}")
        else:
            print("No image found in clipboard")

        return filename

    # def extract_text(filename):
    #     image_path = f"temp/{filename}"
    #     image = Image.open(image_path)
    #     print(image)
    #     # text = pytesseract.image_to_string(image)
    #     # return text

    def extract_text(filename):
        image_path = f"temp/{filename}"
        image = Image.open(image_path)
        print(image)

        # Perform OCR text extraction
        extracted_text = pytesseract.image_to_string(image)
        print(extracted_text)

        return extracted_text
