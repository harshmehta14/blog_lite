from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db=SQLAlchemy()

roles_users = db.Table('roles_users',
                db.Column('user_id',db.Integer(),db.ForeignKey('user.id')),
                db.Column('role_id',db.Integer(),db.ForeignKey('role.id')))

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    followers = db.Column(db.String)
    following = db.Column(db.String)
    total_post=db.Column(db.Integer,default=0)
    last_login= db.Column(db.DateTime)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255),unique=True,nullable=False)
    roles = db.relationship('Role',secondary= roles_users,backref=db.backref('users',lazy='dynamic'))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
   
   
class blogpost(db.Model):
    __tablename__ = 'blogpost'
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description=db.Column(db.String,nullable=False)
    posted_on=db.Column(db.DateTime)
    imgurl=db.Column(db.String)
    posted_by = db.Column(db.String, db.ForeignKey("user.username"), nullable=False)
    likes = db.Column(db.Integer,default=0)
    links=db.Column(db.String)
    # def serialize(self):
    #     return {"id": self.id,
    #             "title": self.title,
    #             "description": self.description,
    #             "posted_on": self.posted_on,
    #             "imgurl": self.imgurl,
    #             "posted_by": self.posted_by,
    #             "likes": self.likes,
    #             "links":self.links
    #             }

 