from flask import Blueprint, render_template, session, request
from images import getImageFromUrl, saveImage
import os
from form_id_handler import formIdHandler
import math

segmentation_bp = Blueprint("segmentation", __name__, url_prefix="/segmentation")

#domain/segmentation
@segmentation_bp.route("/", methods=('GET', 'POST'))
def segmentation():
    if request.method == 'GET':
        def roundUp(num, divisor):
            return math.ceil(num / divisor) * divisor

        divisor = 32 # model says so
        topX = roundUp(int(session["topX"]), divisor)
        topY = roundUp(int(session["topY"]), divisor)
        width = roundUp(int(session["width"]), divisor)
        height = roundUp(int(session["height"]), divisor)
        highlight = (topX, topY, width, height)
        print(f"highlight: {highlight}")

        img_url = session["img_url"]
        img = getImageFromUrl(img_url)
        print(f"Image size: {img.size}")
        saveImage("original", img)

        model_type = session["segModelType"]
        print(f"model type: {model_type}")

        srcpath = os.path.dirname(__file__)
        apppath = os.path.dirname(srcpath)
        modelpath = os.path.join(apppath, 'assets', 'seg_models')
        model_dir = os.path.join(modelpath, "best_fcn16s.pth") \
                    if model_type == "fcn16s" \
                    else \
                    os.path.join(modelpath, "best_unet.pth")
        print(f"model dir: {model_dir}")

        print("Starting segmentation:")
        from segmentation_models import run_inference_from_image as runSeg
        seg_result = runSeg(img, model_dir, model_type, highlight)
        saveImage("seg_result", seg_result)

        # black image, for webdev debugging purposes
        # from PIL import Image
        # seg_result = Image.new('RGB', img.size)
        # saveImage("seg_result", seg_result)

    else: #POST
        form_id = request.form.get("form_id")
        return formIdHandler(form_id)

    return render_template("segmentation.html")