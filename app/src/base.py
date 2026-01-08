from flask import Flask, render_template, redirect, url_for, send_from_directory, request
import os
from form_id_handler import formIdHandler


srcpath = os.path.dirname(__file__)
apppath = os.path.dirname(srcpath)
staticpath = os.path.join(apppath, 'static')
templatepath = os.path.join(apppath, 'templates')
assetspath = os.path.join(apppath, 'assets')

def create_app():
    app = Flask(__name__, static_folder=staticpath, template_folder=templatepath)

    @app.route("/base", methods=('GET', 'POST'))
    def base():
        if request.method == 'POST':
            return formIdHandler(request.form.get('form_id'))
        return render_template("base.html")

    @app.route("/assets/<path:filename>")
    def assets(filename):
        return send_from_directory(assetspath, filename)

    app.secret_key = "secret"

    from user_input import input_bp
    app.register_blueprint(input_bp)

    from inpainting import inpainting_bp
    app.register_blueprint(inpainting_bp)

    from about import about_bp
    app.register_blueprint(about_bp)

    from seg import segmentation_bp
    app.register_blueprint(segmentation_bp)

    @app.route("/")
    def default():
        return redirect(url_for("input.input"))

    return app



if __name__ == "__main__":
    create_app().run(debug=True, host='0.0.0.0')