#Card Image --> Text

import easyocr
import os

reader = easyocr.Reader(['en'])

def extract_text(image_path):
    results = reader.readtext(image_path)

    text = " ".join([r[1] for r in results])

    return text

if __name__ == "__main__":
    image = "sample_card.jpg"

    if os.path.exists(image):
        print(extract_text(image))
