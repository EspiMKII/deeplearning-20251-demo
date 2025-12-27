from flask import Blueprint, render_template, session, request
from images import cropRemainder, saveImage, getImageFromUrl
from form_id_handler import formIdHandler


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
        saveImage("original", img)

        cropped = cropRemainder(img, topX, topY, width, height)
        saveImage("masked", cropped)

        # temp value; modify this later when we need it
        result = img.rotate(180)
        saveImage("output", result)
    else: # POST
        form_id = request.form.get("form_id")
        return formIdHandler(form_id)

    return render_template("inpainting.html")