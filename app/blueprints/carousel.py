from os import scandir
from datetime import datetime
from os.path import join
from time import time
from random import sample
from flask import current_app, request, jsonify, url_for
from . import carouselpage

@carouselpage.route("/")
def carousel():
    count = 0
    files = []

    try:
        count = int(request.args["count"])
    except:
        count = 5     
    for parent in scandir(current_app.config["IMG_DIR"]):
        if parent.is_dir():
            for entry in scandir(join(current_app.config["IMG_DIR"],parent.name)):
                files.append({
                    "name":parent.name,
                    "url":url_for("image.image_file",folder=parent.name,filename=entry.name,_external=True)
                })
    
    if count > len(files):
        return jsonify({
            "error": f"Not enough images. (expected {count}, got {len(files)})",
            "resolution": "Reduce count or add more images."
        })
    return jsonify({
        "version": current_app.config["VERSION"],
        "images": sample(files, count),
        "requested": datetime.fromtimestamp(time()).strftime("%I:%M %p"),
    })