from flask import Blueprint

homepage = Blueprint("home",__name__)
carouselpage = Blueprint("carousel",__name__,url_prefix="/carousel")
imagepage = Blueprint("image",__name__,url_prefix="/image")
healthpage = Blueprint("health",__name__,url_prefix="/health")

from . import home, carousel, image, health