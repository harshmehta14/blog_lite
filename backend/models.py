from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class users(db.Model):
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    followers = db.Column(db.String)
    following = db.Column(db.String)
    total_post=db.Column(db.Integer,default=0)
    last_login= db.Column(db.DateTime)
   
   
class blogpost(db.Model):
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description=db.Column(db.String,nullable=False)
    posted_on=db.Column(db.DateTime)
    imgurl=db.Column(db.String)
    posted_by = db.Column(db.String, db.ForeignKey("users.username"), nullable=False)
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

 