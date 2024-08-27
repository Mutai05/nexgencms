from flask import Flask
from config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    # Set the login view
    login_manager.login_view = 'users.login'
    login_manager.login_message_category = 'info'

    from app.core import core
    app.register_blueprint(core, url_prefix='/')

    from app.admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    from app.users import users
    app.register_blueprint(users, url_prefix='/users')

    from app.blog import blog
    app.register_blueprint(blog, url_prefix='/blog')

    from app.media import media
    app.register_blueprint(media, url_prefix='/media')

    from app.invoices import invoices
    app.register_blueprint(invoices, url_prefix='/invoices')

    from app.database import database
    app.register_blueprint(database, url_prefix='/database')

    from app.users.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app
