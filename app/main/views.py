from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Category
from flask_login import login_required
from .. import db
from .forms import PitchForm,CommentForm
import markdown2

@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = '60 SECOND PITCH !!!'

    
    categories = Category.get_categories()

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

    category = Category.query.get(id)

    if category is None:
        abort(404)
        
    pitches = Pitch.query.filter_by(category_id=id).all()
    print(pitches)
    title = "PITCHES"
    return render_template('category.html', title = title, category=category, pitches = pitches)

@main.route('/pitch/new/', methods = ['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    # category = Category.query.filter_by(id=id).first()

    if form.validate_on_submit():
        pitch = form.content.data
        # category_id = form.category_id.data
        new_pitch = Pitch()

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', new_pitch_form = form, category = category)

@main.route('/pitch/<int:id>', methods = ['GET','POST'])
@login_required
def single_pitch(id):
    '''
    Function the returns a single pitch for comment to be added
    '''

    pitches = Pitch.query.get(id)

    if pitches is None:
        abort(404)

    comment = Comments.get_comments(id)
    title = 'Comment Section'
    return render_template('pitch.html', title = title, pitches = pitches, comment = comment)


    