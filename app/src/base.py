from flask import Flask, render_template, url_for
import os

srcpath = os.path.dirname(__file__)
apppath = os.path.dirname(srcpath)
staticpath = os.path.join(apppath, 'static')
templatepath = os.path.join(apppath, 'templates')
app = Flask(__name__, static_folder=staticpath, template_folder=templatepath)
print(app.static_folder)
print(app.template_folder)

@app.route("/base")
def base():
    return render_template("base.html")

if __name__ == "__main__": app.run(debug=True)