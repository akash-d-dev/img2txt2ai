from PIL import ImageGrab
import os
import time
import uuid
import pytesseract
from PIL import Image


class Screenshot:
    def process_image():
        image = ImageGrab.grabclipboard()

        if not os.path.exists("temp"):
            os.makedirs("temp")

        if image is not None:
            filename = f"{int(time.time())}_{str(uuid.uuid4())[:8]}.png"
            image.save(f"temp/{filename}")
            print(f"Screenshot saved as {filename}")

        return filename

    def extract_text(filename):
        image_path = f"temp/{filename}"
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
