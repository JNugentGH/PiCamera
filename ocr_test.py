import pytesseract
from PIL import Image

img = Image.open("still.jpg")

text = pytesseract.image_to_string(img)

print(text)

