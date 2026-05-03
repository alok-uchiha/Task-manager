from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class TodoForm(FlaskForm):
    title= StringField(
        "title",
        validators=[DataRequired(message="title requried"), Length(min=1, max=100)]
    )
    description= StringField(
        "description",
        validators=[Optional(), Length(max=1000)]
    )
    status= SelectField(
        "status",
        choices=[("pending", "Pending"), ("in_progress", "In Progress"), ("done", "Done")],
        default="in_progress"
    )
    priority= SelectField(
        "priority",
        choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")],
        default="medium"
    )
    due_date= DateField(
        "due_date",
        format="%Y-%m-%d",
        validators=[DataRequired(message="Due date requried")]
    )
    submit= SubmitField(
        "Add task"
    )