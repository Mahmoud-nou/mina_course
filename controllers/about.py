from flask import Blueprint

about = Blueprint("about", __name__)

@about.route("/")
def about_page(lang):
    return "wellco from about page"