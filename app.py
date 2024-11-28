import sqlite3

from flask import *

from models.todos import TodosModel

from controllers.home import home
from controllers.api import api
from controllers.about import about
from controllers.contact import contact
from controllers.update import update_todo
from controllers.profile import profile

from controllers.dashboard.home import dashboard_home
from controllers.dashboard.update import dashboard_update

app = Flask(__name__, template_folder='views')

# Main \   
# path = /AR/Profile/ => what inside the file
home.register_blueprint(profile, url_prefix='/Profile')
# path = /AR/Contact/
home.register_blueprint(contact, url_prefix='/Contact')
# path = /AR/About/
home.register_blueprint(about, url_prefix='/About')
# path = /EN/API/
home.register_blueprint(api, url_prefix='/API')
# path = /AR/
app.register_blueprint(home, url_prefix="/<string:lang>")

# path = / => what inside the file
app.register_blueprint(update_todo)

# Dashboard
# path = /Dashboard/Update/
dashboard_home.register_blueprint(dashboard_update, url_prefix='/Update')
# path = /Dashboard/
app.register_blueprint(dashboard_home, url_prefix='/Dashboard')


@app.route("/")
def home_page():
    return redirect('/AR')

@app.errorhandler(404)
@app.errorhandler(405)
def not_found(e):
    return f"<h1>ERROR: { str(e)[:3] } page</h1>", 404

#############################################################

@app.route("/make_todo", methods=['POST'])
def make_todo():
    if ('make_todo' in request.form
        and 'user_id' in request.form):
        TodosModel.add_data({
            'todo': request.form['make_todo'],
            'user_id': int(request.form['user_id'])
        })
        return redirect('/')
    return 'Not pass'


@app.route("/delete_all/<int:user_id>")
def delete_all(user_id):
    TodosModel.delete_data('"user_id" = '+ str(user_id))
    return redirect('/')


if __name__ == '__main__':
    app.run(
        debug = True,
        port = 80
    )
