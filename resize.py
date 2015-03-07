import string
import imghdr
import random
import os, sys
from os import listdir, path
from os.path import isfile, join
import argparse
from PIL import Image
 
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
 
 
def resizelist(mypath, outputpath, width, height):
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    print onlyfiles
    onlyimagefile = []
    for x in onlyfiles:
        try:
            Image.open(os.path.join(mypath, x))
            onlyimagefile.append(x)
        except:
            pass
    for y in onlyimagefile:
        resize(os.path.join(mypath,y), outputpath, width, height)
    print onlyimagefile
 
def resize(a, b, width, height):
    size = (width, height)
    outfile = os.path.join(b, id_generator() + "." + imghdr.what(a) )
    im = Image.open(a)
    out = im.resize(size)
    out.save(outfile)
 
 
parser = argparse.ArgumentParser()
parser.add_argument("-p","--picture", help="display the resized image")
parser.add_argument("-o","--output", help="image path")
parser.add_argument("-d","--directory", help="path directory")
parser.add_argument("-w","--width", help="image width",
                     type=int)
parser.add_argument("-i","--height", help="image height",
                    type=int)
args = parser.parse_args()
if args.picture:
    resize(args.picture, args.output, args.width, args.height)
elif args.directory:
    resizelist(args.directory, args.output, args.width, args.height)
else:
    print"oh no"
