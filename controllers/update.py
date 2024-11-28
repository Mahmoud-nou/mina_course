from flask import Blueprint, render_template, request, redirect

from models.todos import TodosModel

update_todo = Blueprint('update_todo', __name__, url_prefix='/update_todo')

@update_todo.route("/<int:todo_id>", methods=['POST', 'GET'])
def update_todo_page(todo_id):
    if request.method == 'POST':
        TodosModel.update_data({
            'todo': request.form['update_todo']
        }, todo_id)
        return redirect('/')
    if request.method == 'GET':
        return render_template(
            'update.html',
            todo = TodosModel.get_data_by_pk(todo_id)
        )