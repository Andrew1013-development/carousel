from flask import Blueprint

homepage = Blueprint("home",__name__)
carouselpage = Blueprint("carousel",__name__,url_prefix="/carousel")
imagepage = Blueprint("image",__name__,url_prefix="/image")

from . import home, carousel, image