from PIL import ImageGrab
import os
import time
import uuid
import pytesseract
from PIL import Image
import easyocr


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

    def extract_text(filename):
        image_path = f"temp/{filename}"
        reader = easyocr.Reader(["en"])
        result = reader.readtext(image_path)

        extracted_text = ""
        for detection in result:
            extracted_text += detection[1] + " "

        return extracted_text.strip()
