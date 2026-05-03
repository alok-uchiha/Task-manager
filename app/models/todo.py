from app.extensions import db
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)
    title = db.Column(db.String(100), nullable=False)
    description= db.Column(db.Text, nullable= True)
    status = db.Column(db.Enum("in_progress", "done", "pending"), nullable= False, name="status_enum")
    priority = db.Column(db.Enum("low", "medium", "high"),name="priority_enum", nullable= False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable= False)
    due_date = db.Column(db.DateTime, nullable=False)
    update_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate= datetime.utcnow)
    complete_on = db.Column(db.DateTime, nullable=True)
    deleted_on = db.Column(db.DateTime, nullable=True)

    user = db.relationship('User', backref='todos')
