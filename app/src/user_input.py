from flask import Blueprint, render_template, request, redirect, url_for, session
from coco_data import getRandomUrl

input_bp = Blueprint('input', __name__, url_prefix='/input')

# domain/input
@input_bp.route("/", methods=('GET', 'POST'))
def input():
    url = getRandomUrl()

    if request.method == 'POST':
        session.clear()
        if request.form.get("modeChoice") == "inpainting":
            session["img_url"] = url
            session["topX"] = request.form.get("topX")
            session["topY"] = request.form.get("topY")
            session["width"] = request.form.get("width")
            session["height"] = request.form.get("height")
            return redirect(url_for("inpainting.inpainting"))
        else: #inpainting
            pass

    return render_template("user_input.html", url=url)