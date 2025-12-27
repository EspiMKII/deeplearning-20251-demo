from flask import Blueprint

about_bp = Blueprint('about', __name__, url_prefix='/about')

# domain/about
@about_bp.route('/', methods=('GET', 'POST'))
def about():
    return 'about page'