from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Category(db.Model):
    '''
    Category class define category per pitch
    '''
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    pitches = db.relationship("Pitch", backref = "category", lazy = "dynamic")

    # save
    def save_category(self):
        '''
        Function that saves a category
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        '''
        Function that returns all the data from the categories after being queried
        '''
        categories = Category.query.all()
        return categories

class Pitch(db.Model):
    '''
    List of pitches in each category
    '''

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)

    
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
    pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))    
    comments = db.relationship("Comments", backref="pitch", lazy = "dynamic")


    def save_pitch(self):
        '''
        Save the pitches
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.order_by(Pitch.date_posted.desc()).filter_by(category_id=id).all()
        return pitches

class Comments(db.Model):
    '''
    Comment class that creates new comments from users in pitches
    '''
    __tablename__ = 'comments'

    id = db.Column(db. Integer,primary_key = True)
    comments_section_id = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save_comments(self):
        '''
        Save the comments per pitch
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self,id):
        comments = Comments.query.order_by(Comments.date_posted.desc()).filter_by(pitches_id=id).all()
        return comments

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)

    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)



