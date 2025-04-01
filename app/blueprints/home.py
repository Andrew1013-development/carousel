from flask import redirect, url_for
from . import homepage

@homepage.route("/")
def index():
    return redirect(url_for("carousel.carousel"))