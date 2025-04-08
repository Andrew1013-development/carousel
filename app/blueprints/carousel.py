from os import scandir
from datetime import datetime
from os.path import join
from time import time
from random import sample, randint
from flask import current_app as ca, request, jsonify, url_for
from . import carouselpage

# attempts to curb hidden files detection
def image_check(filename: str) -> bool:
    valid_extensions = (".jpg", ".jpeg", ".png")
    return filename.endswith(valid_extensions)

def image_pick(files: list[dict[str,any]], t: int, count: int) -> list[dict[str,any]]:
    match t:
        case 1:
            # sequential sample
            start_point = randint(0,len(files)-count)
            return files[start_point:start_point+count]
        case 2:
            # randomized sample
            return sample(files, count)

@carouselpage.route("/")
def carousel():
    count = 0
    files = []
    
    # fetch all files
    try:
        count = int(request.args["count"])
    except:
        count = 5     
    for par in scandir(ca.config["IMG_DIR"]):
        if par.is_dir():
            for ent in scandir(join(ca.config["IMG_DIR"],par.name)):
                if image_check(ent.name):
                    files.append({
                        "name":par.name,
                        "url":url_for("image.image_file",folder=par.name,filename=ent.name,_external=True)
                    })
    # validation check
    if count > len(files):
        return jsonify({
            "error": f"Not enough images. (expected {count}, got {len(files)})",
            "resolution": "Reduce count or add more images."
        })
    
    return jsonify({
        "version": ca.config["VERSION"],
        "images": image_pick(files, ca.config["MODE"], count),
        "requested": datetime.fromtimestamp(time()).strftime("%I:%M %p"),
    })