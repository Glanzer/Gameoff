from PIL import Image, ImageFont, ImageDraw, ImageFilter
from io import StringIO, BytesIO
import os

dimensions = [512,512]
colour = [0.0,0.0,0.0]

#package all this into a function.

#print(os.getcwd()+"/Fonts/NovaMono.ttf")

font = ImageFont.truetype(os.getcwd()+"/Fonts/FN0T.TTF",12,0,"unic")
#font = ImageFont.load_default()
#img = Image.open("Testdata/image.jpg")
img = Image.new("RGB",dimensions)

draw = ImageDraw.Draw(img)

draw.text((10,10), "This is some kind of test.\nMONOTYPE. MONOTYPE! Monotype.\n$:", font=font)

ibuffer = BytesIO()
img.save(ibuffer, "PNG")
umg = Image.open(ibuffer)

draw = ImageDraw.Draw(umg)

font = ImageFont.truetype(os.getcwd()+"/Fonts/NovaMono.ttf", 12,0,"unic")

draw.text((10,48), "NOVAMONO:novamono\n$:", font=font, fill=(255,100,200,128))

umg.show()

# ImageFont does the trick for fonts.
# figure out alpha-channels
# figure out effects, animations and stuff to render proper terminals.
