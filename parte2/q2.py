import re

from PIL import Image
import pytesseract

f = open('doc1.bmp', 'rb')
img = Image.open(f)

text = pytesseract.image_to_string(img)
without_spaces = re.sub('\s+', '', text)

print(len(without_spaces))

f.close()
