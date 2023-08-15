from flask import Flask, session
import os
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta
from .test.socket_test import *

def create_app():
    app = Flask(__name__, template_folder= "templates")
    app.config.update(
    DEBUG=True
    )
    app.config.from_pyfile('../config.py')
    socketio.init_app(app)
    csrf = CSRFProtect()
    csrf.init_app(app)
    app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=1)
    
    app.register_blueprint(web_socket)
    
    from .views import main_pages
    app.register_blueprint(main_pages.main)

    from .test import argument
    app.register_blueprint(argument.send_var)

    from .post_get_test import form_post, json_post
    app.register_blueprint(form_post.form_test)
    app.register_blueprint(json_post.json_test)

    from .db_test import mongodb
    app.register_blueprint(mongodb.mongo)
    
    from .flask_wtf_test import form_view
    app.register_blueprint(form_view.form_testing)
    
    from .login_test import login, sign
    app.register_blueprint(login.user_login)
    app.register_blueprint(sign.sign)

    from .board_test import board
    app.register_blueprint(board.board)
    return app