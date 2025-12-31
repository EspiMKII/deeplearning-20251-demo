from flask import Blueprint, render_template, session, request
from images import cropRemainder, saveImage, getImageFromUrl
from form_id_handler import formIdHandler
from COCO_lama import run_inference_from_image
import os

from torch import zeros
from torchvision import transforms

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

        # this is only used for display; the actual mask will be a different object
        cropped = cropRemainder(img, topX, topY, width, height)

        img = img.resize((128, 128))
        saveImage("original", img)

        cropped = cropped.resize((128,128))
        saveImage("masked", cropped)

        # actual mask
        mask = zeros(9, img.height, img.width)
        bottomX, bottomY = topX + width, topY + height
        mask[:, topX:bottomX, topY:bottomY] = 1

        srcpath = os.path.dirname(__file__)
        apppath = os.path.dirname(srcpath)
        assetspath = os.path.join(apppath, 'assets')
        ckpt_path = os.path.join(assetspath, "lightning_logs", "model.ckpt")

        maskedTrash, result, originalTrash = run_inference_from_image(img, mask, ckpt_path)
        # transform = transforms.ToPILImage()
        # result = transform(result.squeeze(0).cpu().detach())

        saveImage("output", result)
    else: # POST
        form_id = request.form.get("form_id")
        return formIdHandler(form_id)

    return render_template("inpainting.html")