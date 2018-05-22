from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Category
from flask_login import login_required
from .. import db
import markdown2

@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = '60 SECOND PITCH !!!'

    categories = Category.query.all()

    # return categories

    return render_template('index.html', title = title, categories = categories)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html", user = user)

@main.route('/lines/')
@login_required
def lines():

    pitches = Pitch.query.get(categories.id)


    return render_template("pitch/pitch.html")