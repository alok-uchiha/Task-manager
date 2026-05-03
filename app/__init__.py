from flask import Flask
from config import Config
from app.extensions import login_manager, bcrypt, db

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.auth.routes import auth
    from app.main.routes import main
    from app.todo.routes import todo
    
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(todo, url_prefix="/todo")

    return app