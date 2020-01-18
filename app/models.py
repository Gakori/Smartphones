from . import db
from datetime import datetime

class User(db.Model):
    '''
    class holding users data
    '''
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    comments = db.relationship('Comment', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Comment(db.Model):
    '''
    holding comments data for users
    '''
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    title = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def save_comment():
        '''
        function that adds,commits and saves comments for the user in the db
        '''
        db.session.add(self)
        db.session.commit()
        
        @classmethod
        def get_comment(cls,id):
            '''
            function that gets comment for a particular user 
            '''
            comments=Comment.query.filter_by(user_id=id).all()
            return comments
    
    def __repr__(self):
        return f"Comments('({self.title})', '{self.date_posted}')"