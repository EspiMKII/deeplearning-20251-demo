from flask import Flask
import os

srcpath = os.path.dirname(__file__)
apppath = os.path.dirname(srcpath)
staticpath = os.path.join(apppath, 'static')
templatepath = os.path.join(apppath, 'templates')
app = Flask(__name__, static_folder=staticpath, template_folder=templatepath)

@app.route("/test")
def test():
    return "man fuck yall"

if __name__ == "__main__": app.run(debug=True)