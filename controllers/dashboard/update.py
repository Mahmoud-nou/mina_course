from flask import Blueprint

dashboard_update = Blueprint("dashboard_update", __name__)

@dashboard_update.route("/")
def dashboard_update_page():
    return "xdgfghjhjkkl"


@dashboard_update.route("/<id>")
def dashboard_update_page_2(id):
    return f"id: {id}"