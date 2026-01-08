from flask import Blueprint, render_template, request, redirect, url_for, session
from coco_data import getRandomUrl
from form_id_handler import formIdHandler

input_bp = Blueprint('input', __name__, url_prefix='/input')

# domain/input
@input_bp.route("/", methods=('GET', 'POST'))
def input():
    url = ""

    if request.method == 'POST':
            form_id = request.form.get("form_id")
            if form_id in ("about", "demo"):
                return formIdHandler(form_id)
            else:
                session["topX"] = request.form.get("topX")
                session["topY"] = request.form.get("topY")
                session["width"] = request.form.get("width")
                session["height"] = request.form.get("height")
                if form_id == "inpainting":
                    return redirect(url_for("inpainting.inpainting"))
                else: #segmentation
                    session["segModelType"] = request.form.get("segModelType")
                    return redirect(url_for("segmentation.segmentation"))


    url = getRandomUrl(samesize=True)
    print(f"Fetching image from {url}")
    session.clear()
    session["img_url"] = url

    return render_template("user_input.html", url=url)