import os
import sys
import string
import imghdr
import random
import argparse

from os import listdir, path
from os.path import isfile, join
from PIL import Image


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--picture", help="path of input image")
parser.add_argument("-o", "--output", help="path of output directory")
parser.add_argument("-d", "--directory", help="path of input directory")
parser.add_argument("-w", "--width", help="image width", type=int)
parser.add_argument("-i", "--height", help="image height", type=int)
parser.add_argument("-l", "--left", help="left coordinate for cropping",
                    type=int)
parser.add_argument("-up", "--upper", help="upper coordinate for cropping",
                    type=int)
parser.add_argument("-r", "--right", help="right coordinate for cropping",
                    type=int)
parser.add_argument("-lo", "--lower", help="lower coordinate for cropping",
                    type=int)
parser.add_argument("-deg", "--degree", help="Degree for rotating",
                    type=int)
parser.add_argument("-ext", "--convert",
                    help="convert any images to any extension")
parser.add_argument("-rz", "--resize", help="For resizing image",
                    action="store_true")
parser.add_argument("-ro", "--rotate", help="For rotating image",
                    action="store_true")
parser.add_argument("-con", "--conversion", help="For extension conversion",
                    action="store_true")
parser.add_argument("-crp", "--cropping", help="For cropping image",
                    action="store_true")
args = parser.parse_args()


class Utility(object):

    """
    An object for some utility functions
    """
    def id_generator(self, size=6,
                     chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def prompt(self):
        if raw_input("Are you sure? [y/N] : ") == "y":
            return True
        else:
            return False

    def ensure_output_dir(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)


class Resize(object):

    """
    An object for resizing images
    """
    def resizelist(self, mypath, outputpath, width, height):
        if Utility().prompt():
            pass
        else:
            return
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        onlyimagefile = []
        for x in onlyfiles:
            try:
                Image.open(os.path.join(mypath, x))
                onlyimagefile.append(x)
            except:
                pass
        for y in onlyimagefile:
            self.resize(os.path.join(mypath, y), outputpath, width, height)

    def resize(self, a, b, width, height):
        utility = Utility()
        size = (width, height)
        outfile = os.path.join(b,
                               utility.id_generator() + "." + imghdr.what(a))
        try:
            im = Image.open(a)
            out = im.resize(size, Image.ANTIALIAS)
            out.save(outfile)
            print "Resized: " + a + "-> " + outfile
        except:
            print "Unable to resize -> " + a


class Rotate(object):
    """
    An object for rotating images
    """
    def rotatelist(self, mypath, outputpath, degree):
        if Utility().prompt():
            pass
        else:
            return
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        onlyimagefile = []
        for x in onlyfiles:
            try:
                Image.open(os.path.join(mypath, x))
                onlyimagefile.append(x)
            except:
                pass
        for y in onlyimagefile:
            self.rotate(os.path.join(mypath, y), outputpath, degree)

    def rotate(self, mypath, outputpath, degree):
        utility = Utility()
        outfile = os.path.join(
            outputpath,
            utility.id_generator() + "." + imghdr.what(mypath))
        try:
            im = Image.open(mypath)
            out = im.rotate(degree)
            out.save(outfile)
            print "Rotated: " + mypath + "-> " + outfile
        except:
            print "Unable to rotate -> " + mypath


class Conversion(object):
    """
    An object for extension conversion
    """
    def extension(self, mypath, outputpath, convert):
        utility = Utility()
        outfilepath = os.path.join(outputpath, utility.id_generator())
        f, e = os.path.splitext(mypath)
        outfile = outfilepath + convert
        if mypath != outfile:
            try:
                Image.open(mypath).save(outfile)
                print "Converted: " + mypath + "-> " + outfile
            except IOError:
                print("unable to convert -> ", mypath)

    def convertlist(self, mypath, outputpath, convert):
        if Utility().prompt():
            pass
        else:
            return
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        onlyimagefile = []
        for x in onlyfiles:
            try:
                Image.open(os.path.join(mypath, x))
                onlyimagefile.append(x)
            except:
                pass
        for y in onlyimagefile:
            self.extension(os.path.join(mypath, y), outputpath, convert)


class Crop(object):
    """
    An object for cropping image
    """
    def crop(self, mypath, outputpath, left, upper, right, lower):
        utility = Utility()
        box = (int(left), int(upper), int(right), int(lower))
        outfile = os.path.join(
            outputpath,
            utility.id_generator() + "." + imghdr.what(mypath))
        im = Image.open(mypath)
        try:
            region = im.crop(box)
            region.save(outfile)
            print "Cropped: " + mypath + "-> " + outfile
        except:
            print "Unable to crop -> ", mypath

    def croplist(self, mypath, outputpath, left, upper, right, lower):
        if Utility().prompt():
            pass
        else:
            return
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        onlyimagefile = []
        for x in onlyfiles:
            try:
                Image.open(os.path.join(mypath, x))
                onlyimagefile.append(x)
            except:
                pass
        for y in onlyimagefile:
            self.crop(os.path.join(mypath, y),
                      outputpath, left, upper, right, lower)


if __name__ == "__main__":
    resize, rotate = Resize(), Rotate()
    convert, crop = Conversion(), Crop()
    Utility().ensure_output_dir(args.output)
    if args.resize:
        if args.picture:
            resize.resize(args.picture, args.output, args.width, args.height)
        elif args.directory:
            resize.resizelist(args.directory,
                              args.output, args.width, args.height)
    elif args.rotate:
        if args.picture:
            rotate.rotate(args.picture, args.output, args.degree)
        elif args.directory:
            rotate.rotatelist(args.directory, args.output, args.degree)
    elif args.conversion:
        if args.picture:
            convert.extension(args.picture, args.output, args.convert)
        elif args.directory:
            convert.convertlist(args.directory, args.output, args.convert)
    elif args.cropping:
        if args.picture:
            crop.crop(args.picture, args.output, args.left,
                      args.upper, args.right, args.lower)
        elif args.directory:
            crop.croplist(args.directory, args.output,
                          args.left, args.upper, args.right, args.lower)
    else:
        print "Use -h for help section"
