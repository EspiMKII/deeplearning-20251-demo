import os
import json
from random import choice

# We're using the 2017 Testing Image subset from COCO for our job, because that seems pretty light

# all of this was to just save the urls somewhere more convenient instead of using the annotation file from COCO
srcpath = os.path.dirname(__file__)
apppath = os.path.dirname(srcpath)
datapath = os.path.join(apppath, 'assets', 'data')
annotationpath = os.path.join(datapath, 'annotations')

targetfile = 'image_info_test2017.json'
targetpath = os.path.join(annotationpath, targetfile)

# with open(targetpath) as f:
#     annotations = json.load(f)
# img_urls = [image["coco_url"] for image in annotations["images"]]
# f.close()

urllist_path = os.path.join(datapath, "url.json")
# with open(urllist_path, "w") as f:
#     json.dump(img_urls, f)

# here are the actually useful stuff
def openUrlList():
    with open(urllist_path, "r") as f:
        return json.load(f)

def getRandomUrl(urllist=None):
    if urllist == None: urllist = openUrlList()
    return choice(urllist)

def getImage(url=None):
    if url == None: url = getRandomUrl()
    from PIL import Image
    from urllib.request import urlopen
    return Image.open(urlopen(url))

if __name__ == "__main__":
    img = getImage()
    img.show()