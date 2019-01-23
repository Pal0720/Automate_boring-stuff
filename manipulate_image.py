#!python3

import os
from PIL import Image

#load the logo
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_image = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_image.size

#make new directory and loop over every file to check if it is an image
os.makedirs('with_logo', exist_ok=True) #exist_ok=True will keep from raising an exception if folder name already present
for filename in os.listdir('.'):
    if not (filename.endswith('\.png') or filename.endswith('.\jpg')) or filename == LOGO_FILENAME:
        continue #skip non-image files and the logo file itself

im = Image.open(filename)
width, height = im.size

#Resize the images
#check if images need resizing
if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
    if  width > height :
        height = int((SQUARE_FIT_SIZE/width) * height)
        width = SQUARE_FIT_SIZE
    else:
        width = int((SQUARE_FIT_SIZE/height) * width)
        height = SQUARE_FIT_SIZE

    #Resize
    print("resizing... {}".format(filename))
    im = im.resize((width,height))

# Add the logo and save the changes
print("Adding logo to : {}".format(filename))

im.paste(logo_image,(width - logo_width, height - logo_height),logo_image)

#save changes
im.save(os.path.join('with_logo',filename))
