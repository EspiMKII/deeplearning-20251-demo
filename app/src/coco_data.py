import os
import json
from random import choice

# We're using the 2017 Testing Image subset from COCO for our job, because that seems pretty light

srcpath = os.path.dirname(__file__)
apppath = os.path.dirname(srcpath)
datapath = os.path.join(apppath, 'assets', 'data')
annotationpath = os.path.join(datapath, 'annotations')

# there is also a file named  image_info_test-dev2017.json, but we're not using that
targetfile = 'image_info_test2017.json'
targetpath = os.path.join(annotationpath, targetfile)

urllist_path = os.path.join(datapath, "url.json")
samesize_urllist_path = os.path.join(datapath, "samesize_url.json")

# creating json files with just links, for convenience
# comment out as necessary
# with open(targetpath) as f:
#     annotations = json.load(f)
# img_urls = [image["coco_url"] for image in annotations["images"]]
# f.close()
# with open(urllist_path, "w") as f:
#     json.dump(img_urls, f)

# with open(targetpath) as f:
#     annotations = json.load(f)
# same_size_img_urls = []
# for image in annotations["images"]:
#     if image["width"] == image["height"]:
#         same_size_img_urls.append(image["coco_url"])
# with open(samesize_urllist_path, "w") as f:
#     json.dump(same_size_img_urls, f)

# # here are the actually useful stuff
def openUrlList(urllist_path):
    with open(urllist_path, "r") as f:
        return json.load(f)

def getRandomUrl(samesize=True):
    '''
    Parameters:
        samesize (bool): guarantees the image from the url is of same width and height
    '''
    if samesize:
        print(f"If this function sees the url file, it will obviously know it is as {samesize_urllist_path}")
        urllist = openUrlList(samesize_urllist_path)
    else:
        urllist = openUrlList(urllist_path)
    return choice(urllist)

if __name__ == "__main__":
    from images import getImageFromUrl, cropRemainder, saveImage
    url = getRandomUrl(samesize=True)
    img = getImageFromUrl(url)
    # saveImage("img", img)
    img.show()

    cropped = cropRemainder(img, 100, 100, 100, 100)
    # saveImage("cropped", cropped)
    cropped.show()