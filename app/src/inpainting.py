from flask import Blueprint, render_template, session
from coco_data import getImage


inpainting_bp = Blueprint('inpainting', __name__, url_prefix='/inpainting')

# domain/inpainting
@inpainting_bp.route("/")
def inpainting():
    topX = int(session["topX"])
    topY = int(session["topY"])
    width = int(session["width"])
    height = int(session["height"])

    # testing values
    if (not topX) | (not topY) | (not width) | (not height):
        session.clear()
        topX, topY, width, height = 100, 100, 100, 100

    img_url = session["img_url"]
    img = getImage(img_url)


    return render_template("inpainting.html",
                            img_url=img_url
    )