from os.path import join
from flask import current_app, send_from_directory
from . import imagepage

@imagepage.route("/<folder>/<filename>")
def image_file(folder: str, filename: str):
    return send_from_directory(join(current_app.config["IMG_DIR"],folder),filename)