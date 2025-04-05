from os import environ
from dotenv import load_dotenv
from flask import Flask

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config["IMG_DIR"] = environ["IMG_DIR"]
    app.config["VERSION"] = "v0.2.3"

    from .blueprints import carouselpage, imagepage, homepage
    app.register_blueprint(carouselpage)
    app.register_blueprint(imagepage)
    app.register_blueprint(homepage)

    return app