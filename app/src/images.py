from PIL import Image
from coco_data import getRandomUrl
import os

def getImageFromUrl(url: str):
    if url == None: url = getRandomUrl()
    from urllib.request import urlopen
    return Image.open(urlopen(url))

def cropRemainder(
    img: Image.Image,
    topX: int,
    topY: int,
    width: int,
    height: int
):
    """
    so you know how ImageInstance.crop(box) crops out that specific part of the image?\n
    this achieves 2 new things:\n
    firstly, uses these 4 parameters as input, instead of a 4-tuple to define the crop box\n
    secondly, instead of getting the cropped part, we're getting the REMAINDER of the image
    AFTER the crop\n
    Follows the conventional coordination of Pillow's image manipulation tools:
    top left of image is (0,0), positive X is to the right, positive Y is downwards
    """

    # converts the 4 parameters to a 4-tuple defining the box
    left = topX
    upper = topY
    right = topX + width
    lower = topY + height

    result = Image.new("RGB", img.size)

    # top part
    top_box = (0, 0, img.width, upper)
    result.paste(img.crop(top_box), top_box)
    # left part
    left_box = (0, upper, left, lower)
    result.paste(img.crop(left_box), left_box)
    # right part
    right_box = (right, upper, img.width, lower)
    result.paste(img.crop(right_box), right_box)
    # bottom part
    bottom_box = (0, lower, img.width, img.height)
    result.paste(img.crop(bottom_box), bottom_box)

    # result
    return result

def saveImage(
    targetname: str,
    img: Image.Image,
):
    srcpath = os.path.dirname(__file__)
    apppath = os.path.dirname(srcpath)
    assetspath = os.path.join(apppath, "assets")
    targetfile = targetname + ".jpg" # /shrug
    targetdir = os.path.join(assetspath, targetfile)

    if os.path.exists(targetdir):
        os.remove(targetdir)
    img.save(targetdir)

    return