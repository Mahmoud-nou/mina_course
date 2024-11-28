from flask import Blueprint, render_template, abort

from config import vars

dashboard_home = Blueprint('dashboard_home', __name__)

@dashboard_home.route("/")
def dashboard_home_page():
    return "hello from dashboard"

  