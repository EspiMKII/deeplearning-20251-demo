from flask import Blueprint, render_template, session, request
from images import cropRemainder, saveImage, getImageFromUrl
from form_id_handler import formIdHandler
from COCO_lama import run_inference_from_image, tensor2PILImage
import os

from torch import zeros

inpainting_bp = Blueprint('inpainting', __name__, url_prefix='/inpainting')

# domain/inpainting
@inpainting_bp.route("/", methods=('GET', 'POST'))
def inpainting():
    if request.method == 'GET':
        topX = int(session["topX"])
        topY = int(session["topY"])
        width = int(session["width"])
        height = int(session["height"])

        # # testing values
        # if (not topX) | (not topY) | (not width) | (not height):
        #     session.clear()
        #     topX, topY, width, height = 100, 100, 100, 100

        img_url = session["img_url"]
        print(f"retrieved url from session: {img_url}")
        img = getImageFromUrl(img_url)
        oldwidth, oldheight = img.width, img.height
        img = img.resize((128, 128))
        saveImage("original", img)

        # rescaling as we just resized the image
        topX = topX * 128 // oldwidth
        topY = topY * 128 // oldheight
        width = width * 128 // oldwidth
        height = height * 128 // oldheight

        # this is only used for display; the actual mask will be a different object
        cropped = cropRemainder(img, topX, topY, width, height)
        saveImage("masked", cropped)

        # actual mask
        mask = zeros(9, img.height, img.width)
        bottomX, bottomY = topX + width, topY + height
        mask[:, topY:bottomY, topX:bottomX] = 1

        srcpath = os.path.dirname(__file__)
        apppath = os.path.dirname(srcpath)
        assetspath = os.path.join(apppath, 'assets')
        ckpt_path = os.path.join(assetspath, "lightning_logs", "model.ckpt")

        maskedTrash, result, originalTrash = run_inference_from_image(image=img, mask=mask, ckpt_path=ckpt_path)

        result = tensor2PILImage(result)

        saveImage("output", result)
    else: # POST
        form_id = request.form.get("form_id")
        return formIdHandler(form_id)

    return render_template("inpainting.html")