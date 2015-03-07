import string
import random
import os, sys
import argparse
from PIL import Image

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def resize(a, b, width, height):
    size = (width, height)
    outfile = os.path.join(b, id_generator() + ".jpg" )
    im = Image.open(a)
    out = im.resize(size)
    out.save(outfile, "JPEG")


parser = argparse.ArgumentParser()
parser.add_argument("-p","--picture", help="display the resized image")
parser.add_argument("-o","--output", help="image path")
parser.add_argument("-w","--width", help="image width",
                     type=int)
parser.add_argument("-i","--height", help="image height",
                    type=int)
args = parser.parse_args()
if args.picture:
    resize(args.picture, args.output, args.width, args.height)
else:
    print "Some error"



