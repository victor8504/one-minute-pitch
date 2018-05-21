from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from flask_login import login_required
from .. import db
import markdown2

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html", user = user)