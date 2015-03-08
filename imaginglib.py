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

def crop(mypath, outputpath, left, upper, right, lower):
    box = (left, upper, right, lower)
    outfile = os.path.join(outputpath, id_generator() + "." + imghdr.what(mypath) )
    im = Image.open(mypath)
    try:
        region = im.box(crop)
        region.save(outfile)
    except:
        print "Enter proper coordinates"

def croplist(mypath, outputpath, left, upper, right, lower):
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
        crop(os.path.join(mypath,y), outputpath, left, upper, right, lower)
    print onlyimagefile

def extension(mypath, outputpath, convert):
    outfilepath = os.path.join(outputpath, id_generator() )
    f, e = os.path.splitext(mypath)
    outfile = outfilepath + convert
    print convert
    print outfile
    if mypath != outfile:
        try:
            Image.open(mypath).save(outfile)
        except IOError:
            print("cannot convert", mypath)
def convertlist(mypath, outputpath, convert):
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
        extension(os.path.join(mypath,y), outputpath, convert)
    print onlyimagefile

def rotate(mypath, outputpath, degree):
    outfile = os.path.join(outputpath, id_generator() + "." + imghdr.what(mypath) )
    im = Image.open(mypath)
    out = im.rotate(degree)
    out.save(outfile) 

def rotatelist(mypath, outputpath, degree):
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
        rotate(os.path.join(mypath,y), outputpath, degree)
    print onlyimagefile

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
parser.add_argument("-rz","--resize", help="image to be resize",
                    action="store_true")
parser.add_argument("-ro","--rotate", help="image to rotate",
                    action="store_true")
parser.add_argument("-con","--conversion", help="images to convert extension",
                    action="store_true")
parser.add_argument("-crp","--cropping", help="image to be cropped",
                    action="store_true")
parser.add_argument("-p","--picture", help="display the resized image")
parser.add_argument("-o","--output", help="image path")
parser.add_argument("-d","--directory", help="path directory")
parser.add_argument("-ext","--convert", help="convert any images to any extension")
parser.add_argument("-w","--width", help="image width",
                     type=int)
parser.add_argument("-i","--height", help="image height",
                    type=int)
parser.add_argument("-deg","--degree", help="rotate image to a degree",
                    type=int)
parser.add_argument("-l","--left", help="image to be crop from left",
                    type=int)
parser.add_argument("-up","--upper", help="image to be crop from upper",
                    type=int)
parser.add_argument("-r","--right", help="image to be crop from right",
                    type=int)
parser.add_argument("-lo","--lower", help="image to be crop from lower",
                    type=int)
args = parser.parse_args()
if args.resize:
    if args.picture:
        resize(args.picture, args.output, args.width, args.height)
    elif args.directory:
        resizelist(args.directory, args.output, args.width, args.height)
elif args.rotate:
    if args.degree:
        if args.picture:
            rotate(args.picture, args.output, args.degree)
        elif args.directory:
            rotatelist(args.directory, args.output, args.degree)
elif args.conversion:
    if args.convert:
        if args.picture:
            extension(args.picture, args.output, args.convert)
        elif args.directory:
            convertlist(args.directory, args.output, args.convert)
elif args.cropping:
    if args.picture:
        crop(args.picture, args.output, args.left, args.upper, args.right, args.lower)
    elif args.directory:
        croplist(args.directory, args.output, args.left, args.upper, args.right, args.lower)
