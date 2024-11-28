from flask import Blueprint

contact = Blueprint("contact", __name__)

@contact.route("/")
def contact_page(lang):
    return "wellco from contact"