import flask
import flask_login
from main.settings import db
from flask_login import logout_user
from registration.models import User

def render_home():
    return flask.render_template(template_name_or_list='home.html', users = User.query.all(), is_auth = flask_login.current_user.is_authenticated)

def render_logout():
    logout_user()
    return flask.redirect('/')