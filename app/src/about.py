from flask import Blueprint, render_template, request
from form_id_handler import formIdHandler

about_bp = Blueprint('about', __name__, url_prefix='/about')

# domain/about
@about_bp.route('/', methods=('GET', 'POST'))
def about():
    if request.method == "POST":
        form_id = request.form.get("form_id")
        return formIdHandler(form_id)
    return render_template("about.html")