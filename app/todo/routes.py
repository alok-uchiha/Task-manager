from flask import Blueprint, render_template, jsonify
from app.todo.forms import TodoForm
from app.models.todo import Todo
from flask_login import login_required, current_user
from app.extensions import db

todo = Blueprint("todo", __name__)


@todo.route("/")
@login_required
def dashboard():

    form = TodoForm()

    todos = Todo.query.filter_by(user_id=current_user.id).all()

    return render_template("todo/dashboard.html", form= form, todos=todos)

@todo.route("/create", methods=["POST"])
@login_required
def create():

    form= TodoForm()

    if form.validate_on_submit():
        new_todo= Todo(
            title= form.title.data,
            description= form.description.data,
            status= form.status.data,
            priority= form.priority.data,
            due_date= form.due_date.data,
            user_id = current_user.id
        )

        db.session.add(new_todo)
        db.session.commit()
        return jsonify({
            'success' : True,
            "todo" : {
                "id" : new_todo.id,
                "title" : new_todo.title
            }
        })
    return jsonify({"success": False, "error" : form.errors}), 400