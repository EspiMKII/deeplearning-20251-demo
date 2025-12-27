from PIL import Image
from coco_data import getRandomUrl

def getImage(url=None):
    if url == None: url = getRandomUrl()
    from urllib.request import urlopen
    return Image.open(urlopen(url))

def cropRemainder(img, topX, topY, width, height):
    # so you know how ImageInstance.crop(box) crops out that specific part of the image?
    # this achieves 2 new things:
    # firstly, uses these 4 parameters as input, instead of a 4-tuple to define the crop box
    # secondly, instead of getting the cropped part, we're getting the REMAINDER of the image
    # AFTER the crop


    # converts the 4 parameters to a 4-tuple defining the box


    result = Image.new(mode=)


    # top part

    # left part

    # right part

    # bottom part

    # result
    return result