from flask import Blueprint, redirect, render_template, request, url_for
from models.todo import todo

action = Blueprint("action", __name__, static_folder="../static", template_folder="../templates")

@action.route('/', methods=['GET'])
def index():
    listofall = todo.get_all()
    tododict = [t.to_dict() for t in listofall]
    return render_template("todo_list.html", todos = tododict)

@action.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template("add_todo.html")

    title = request.form['title']
    content = request.form['content']
    status = request.form.get('status', 'pending')
    todo.create(title, content, status)
    return redirect(url_for('action.index'))

@action.route('/remove', methods = ['GET', 'POST'])
def remove():
    listofall = todo.get_all()
    tododict = [t.to_dict() for t in listofall]
    if request.method == "GET":
        return render_template('remove.html', todoid = tododict)
    else:
        id = int(request.form['id'])
        todo.delete(id)
        return redirect(url_for('action.index'))
    
@action.route('/edit', methods = ['GET', 'POST'])
def edit():
    listofall = todo.get_all()
    tododict = [t.to_dict() for t in listofall]
    if request.method == 'GET':
        return render_template('edit.html', todoid = tododict)
    else:
        id = int(request.form['id'])
        title = request.form['title']
        content = request.form['content']
        status = bool(request.form.get('status'))
        todo.update(title, content, status, id)
        return redirect(url_for('action.index'))