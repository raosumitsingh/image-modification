import os, sys
from PIL import Image

size = (128, 128)

for infile in os.listdir("C:\\Users\\sumit kumar\\Desktop\\Image modification\\images"):
    outfile = os.path.splitext(infile)[0]
    try:
        with Image.open(infile).convert('RGB') as im:
            im.thumbnail(size)
            im.rotate(270).save(r"C:\Users\sumit kumar\Desktop\Image modification\result\\" + outfile, "JPEG")
    except OSError:
        pass
