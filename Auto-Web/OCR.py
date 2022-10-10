import pytesseract
from PIL import Image # pip install pillow
import os

path = os.getcwd()

# image = Image.open('pantip-post.png')
image = Image.open('article.png')

print(pytesseract.image_to_string(image, lang='tha'))
