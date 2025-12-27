from flask import redirect, url_for

def formIdHandler(form_id):
    map = {
        "demo": "default",
        "about": "about.about",
        "again": "default"
    }

    return redirect(url_for(map[form_id]))