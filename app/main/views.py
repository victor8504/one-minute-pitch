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

    return render_template('index.html', title = title, categories = categories)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html", user = user)

@main.route('/category/<int:id>')
@login_required
def category(id):
    '''
    a route function that returns a list of pitches as per category chosen and 
    allows users to create a new pitch
    '''

    categories = Category.query.get(id)

    if category is None:
        abort(404)
        
    pitches = Pitch.get_pitches(id)
    title = "PITCHES"
    return render_template('category.html', title = title, categories = categories, pitches = pitches)

    