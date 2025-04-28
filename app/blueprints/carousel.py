from os import scandir
from datetime import datetime
from os.path import join
from time import time
from random import sample, randint
from flask import current_app as ca, request, jsonify, url_for
from . import carouselpage

# attempts to curb hidden files detection
def image_check(filepath: str) -> bool:
    # magic numbers sourced from https://en.wikipedia.org/wiki/List_of_file_signatures
    magic_numbers = {
        ".png": bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
        ".jpg": bytes([0xFF, 0xD8, 0xFF]), # omitted 4th byte and beyond
        ".bmp": bytes([0x42, 0x4D]),
        ".gif": bytes([0x47, 0x49, 0x46]),
        ".webp": bytes([0x52, 0x49, 0x46, 0x46]), # only used first 4 bytes
    }
    f = open(filepath, "rb") 
    file_id = f.read(8) # read first 8 bytes
    f.close()
    for extension in magic_numbers:
        if file_id.startswith(magic_numbers[extension]):
            return True
    return False

def image_pick(files: list[dict[str,str]], t: int, count: int) -> list[dict[str,str]] | None:
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
                if image_check(ent.path):
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