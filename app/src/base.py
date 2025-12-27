from flask import Flask, render_template, redirect, url_for
import os

srcpath = os.path.dirname(__file__)
apppath = os.path.dirname(srcpath)
staticpath = os.path.join(apppath, 'static')
templatepath = os.path.join(apppath, 'templates')

def create_app():
    app = Flask(__name__, static_folder=staticpath, template_folder=templatepath)

    @app.route("/base")
    def base():
        return render_template("base.html")

    app.secret_key = "secret"

    from user_input import input_bp
    app.register_blueprint(input_bp)

    from inpainting import inpainting_bp
    app.register_blueprint(inpainting_bp)

    @app.route("/")
    def default():
        return redirect(url_for("input.input"))

    return app



if __name__ == "__main__": create_app().run(debug=True)