# imaginglib
 
A python script which give some features to apply to a image or so many images.Features like resizing an image or a group of images, rotating features, cropping or if we want to change extension of any images.
 
## Configuring This Package
 
Install system dependencies: ``$ sudo yum install Pillow``
 
Clone this repository using this command:-
   
    git clone https://github.com/shiminsh/imaginglib.git
 
Now, change into the directory `imaginglib` using this command:-
   
    cd imaginglib/
 
And run this command to get all information how to use features:-
   
    $ python imaginglib.py -h
 
Commands:-
 
-rz  : used for resizing image.
-ro  : used for rotating image.
-con : used for converting extension of image.
-crp : used for cropping image.
-p   : used for giving path of an image.
-d   : used for giving path of directory containg images.
-o   : used for giving path of directory in which images got saved after any operation.
 
## For Resizing
 
    -w : used for width, provide width of image you want in place of <width> after -w.
    -i : used for height, provide height of image you want in place of <height> after -w.
 
### For one image
 
    ``$ python imaginglib.py -rz -p </path/of/input/image> -o </path/of/input/directory/> -w <width> -i <height>``
 
### For images in a directory
 
    ``$ python imaginglib.py -rz -d </path/of/input/directory/> -o </path/to/output/directory/> -w <width> -i <height>``
 
## For Rotating Images
 
    -deg : used for degree, provide degree for rotation inplace of <degree> after -deg.
 
### For one image
 
    ``$ python imaginglib.py -ro -p </path/of/input/image> -o </path/to/output/directory/> -deg <degree>``
 
### For images in a directory
 
    ``$ python imaginglib.py -ro -d </path/of/input/directory/> -o </path/to/output/directory/> -deg <degree>``
 
## For Converting extension of Images
 
    -ext : used for extension, provide extension in which you want image to convert in place of <.extension> after -ext.
    for example: -ext .png
 
### For one image
 
    ``$ python imaginglib.py -con -p </path/of/input/image> -o </path/to/output/directory/> -ext <.extension>``
 
### For images in a directory
 
    ``$ python imaginglib.py -con -d </path/of/input/directory/> -o </path/to/output/directory/> -ext <.extension>``
 
## For Cropping Image
   
    The region is defined by a 4-tuple, where coordinates are (left, upper, right, lower). The Python Imaging Library uses a coordinate system with (0, 0) in the upper left corner.
    -l : used for left coordinate, provide left coordinate inplace of <left> after -l.
    -up : used for upper coordinate, provide upper coordinate inplace of <upper> after -up.
    -r : used for right coordinate, provide right coordinate inplace of <right> after -r.
    -lo : used for lower coordinate, provide lower coordinate inplace of <lower> after -lo.
 
### For one image
 
    ``$ python imaginglib.py -crp -p </path/of/input/image> -o </path/to/output/directory/> -l <left> -up <upper> -r <right> -lo <lower>``
 
### For images in a directory
 
    ``$ python imaginglib.py -crp -d </path/of/input/directory/> -o </path/to/output/directory/> -l <left> -up <upper> -r <right> -lo <lower>``
