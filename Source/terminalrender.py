#! /bin/python

from PIL import Image, ImageDraw
from io import StringIO, BytesIO

#dimensions = (512,512)

img = Image.open("Testdata/image.jpg")

ibuffer = BytesIO()
img.save(ibuffer, "PNG")
umg = Image.open(ibuffer)
umg.show()

# initialize array for the spritesheet and find out if just storing all the values is more efficient than parsing the spritesheet anew every time.
