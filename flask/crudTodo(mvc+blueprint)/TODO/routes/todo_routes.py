from flask import Blueprint, redirect, render_template, request
from models.todo import todo

action = Blueprint("action", __name__, url_prefix='/todos',static_folder="../static", template_folder="../templates")

@action.route('/')
def index():
    return render_template("index.html")

@action.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template("add_todo.html")

    title = request.form['title']
    content = request.form['content']
    status = bool(request.form.get('status', False))
    todo.create(title, content, status)
    return 'aded'