from flask import Blueprint, render_template, url_for

input_bp = Blueprint('input', __name__, url_prefix='/input')

@input_bp.route("/input")
def input():
    return render_template("input.html")
