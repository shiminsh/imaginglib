import os, sys
import argparse
from PIL import Image
 
size = (1280, 1380)
outfile= "/home/shalini/shalu.jpg"
 
def resize(a, size, outfile):
    im = Image.open(a)
    im.thumbnail(size)
    im.save(outfile, "JPEG")
 
 
parser = argparse.ArgumentParser()
parser.add_argument("-p","--picture", help="display the resized image")
args = parser.parse_args()
if args.picture:
    resize(args.picture, size, outfile)
else:
    print "Oh no"
