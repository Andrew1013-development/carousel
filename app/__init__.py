from json import load as json_load
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_file("config.json", load=json_load)
    app.config["VERSION"] = "v0.2.4"

    from .blueprints import carouselpage, imagepage, homepage
    app.register_blueprint(carouselpage)
    app.register_blueprint(imagepage)
    app.register_blueprint(homepage)

    return app