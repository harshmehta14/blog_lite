import os
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from models import *
import datetime
from flask_security import Security, SQLAlchemySessionUserDatastore, hash_password, auth_required, current_user
from config import LocalDevelopmentConfig


app=None
api=None

def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config.from_object(LocalDevelopmentConfig)
  db.init_app(app)
  app.app_context().push()
  user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
  security = Security(app, user_datastore)
  api = Api(app)
  app.app_context().push()
  with app.app_context():
    db.create_all()
  return app, api
  # return app

app,api = create_app()


# from controller import *

from api import *
api.add_resource(UserAPI,"/api/user","/api/user/<username>")

# app= create_app()

# @app.route('/')
# @auth_required('token')
# def home():
#   if current_user.is_authenticated:
#     return current_user.email
#   else:
#     return "Login "


# @app.route('/login',methods=['POST'])
# def login():
#   try:
#     data = request.json
#     email = data['email']
#     password= data['password']
#     if users.query.filter_by(email=email,password=password).first():
#         username= users.query.filter_by(email=email,password=password).first()
#         username.last_login = datetime.datetime.now()
#         db.session.commit()
#         return jsonify({"login":"success"})
#     else:
#         return jsonify({"login":"failed"})
#   except Exception as e:
#     return jsonify({"login":"failed"})


# @app.route('/register',methods=['POST'])
# def signup():
#   try:
#     data = request.json
#     email = data['email']
#     password= data['password']
#     username = data['username']success
#     print(email,password,username)
#     user = Users(
#       email=email,
#       username=username,
#       password=password,
#       last_login=datetime.datetime.now(),
#       )
#     db.session.add(user)
#     db.session.commit()
#     return jsonify({"signup":"success"})
#   except Exception as e:
#     return jsonify({"signup":e})


#_____________________MY PROFILE _________________________
#givies information about any username supplied to it
#login required
@app.route('/profile',methods=['GET'])
@auth_required('token')
def profile():
  try:
    # print(current_user.username)
    # username1 = current_user.username
    user = User.query.filter_by(username=current_user.username).first()
    # print(users.last_login)
    # followers = "" if user.followers == None else user.followers.split(',')
    # following = "" if user.following == None else user.following.split(',')
    last_login = "" if user.last_login == None else user.last_login

    # print(user.last_login)
    return jsonify({"profile":True,'total_posts':user.total_post,'email':user.email,"last_login":last_login,"username":user.username}),200
  except Exception as e:
    return jsonify({"profile":False})
  
# give out blogs of all following friend of given user
# login required

#_____________________MY PROFILE END _________________________


# ______________________________HOME PAGE __________________________________________
@app.route('/getblogs',methods=['GET'])
@auth_required('token')
def getblogs():
  try:
    user_id = current_user.id
    posts=[]
    a = "asc"
    query = blogpost.posted_on.desc() if a =="desc" else blogpost.posted_on.asc()
    user_following_list = []

    #_____List of all people who user is following____
    Followers_list= Followers.query.filter_by(followers = user_id).all()
    # print(Followers_list)

    #_____List of all user for fetching Names____
    users= User.query.all()
    for follow in Followers_list:
      for user in users:
        if str(user.id) == str(follow.following):
          user_following_list.append(user.username)
  
    user_following_list = list(set(user_following_list))
    # print(user_following_list)

    blogs = blogpost.query.filter_by(private_public="0").order_by(query).all()
    # print(blogs)

    for blog in blogs:
      if blog.posted_by in user_following_list:
        posts.append({"blog_id":blog.id,
                      "title":blog.title,
                      "description":blog.description,
                      "posted_on":blog.posted_on,
                      "likes":blog.likes,
                      "posted_by":blog.posted_by,
                      "links":blog.links,
                      "imgurl":blog.imgurl,
                      "private_public":blog.private_public,})
        
    # print(posts)
    return posts
    # return jsonify({'total_posts':user.total_post,"followers": user.followers,'following':user.following,'email':user.email,"last_login":user.last_login,"username":user.username}),200
  except Exception as e:
    return jsonify([])



# gives top 5 trending blogs 
# login NOT required 
@app.route('/gettrendingblogs',methods=['GET'])
def gettrendingblogs():
  try:
    posts=[]
 
    blogs = blogpost.query.filter_by(private_public="0").order_by(blogpost.likes.desc()).all()
    # print(blogs[0:5])
    for blog in blogs[0:5]:
      # print(blog.title)
      posts.append({"blog_id":blog.id,
                    "title":blog.title,
                    "description":blog.description,
                    "posted_on":blog.posted_on,
                    "likes":blog.likes,
                    "posted_by":blog.posted_by,
                    "links":blog.links,
                    "imgurl":blog.imgurl,})
    return jsonify(posts)
    # return jsonify({'total_posts':user.total_post,"followers": user.followers,'following':user.following,'email':user.email,"last_login":user.last_login,"username":user.username}),200
  except Exception as e:
    return make_response(e, 403)

@app.route('/like_post',methods=['GET'])
@auth_required('token')
def like_post():
  try:
    blog_id = request.args["blog_id"]
    blog = blogpost.query.filter_by(id=blog_id).first()
    blog.likes += 1
    db.session.commit()
    return jsonify({"liked":"sucess"})
  except Exception as e:
    return jsonify({"liked":"fail"})
# ______________________________HOME PAGE END__________________________________________




#________________________________MY POST ____________________________________________


    
# give out blogs of a particular user
@app.route('/crud_user_post',methods=['GET','DELETE'])
@auth_required('token')
def crud_user_post():
  username = current_user.username
  if request.method == "GET":
    try:
      # print(username)
      posts=[]
      # user_following =  users.query.filter_by(username=username).first()
      # user_following = user_following.following.split(',')
      # print(user_following[0:len(user_following)-1])
      blogs = blogpost.query.filter_by(posted_by=username).all()
      if blogs != None:
        for blog in blogs:
            # print(blog.id)
            posts.append({"blog_id":blog.id,
                          "title":blog.title,
                          "description":blog.description,
                          "posted_on":blog.posted_on,
                          "likes":blog.likes,
                          "posted_by":blog.posted_by,
                          "links":blog.links,
                          "imgurl":blog.imgurl,
                          "private_public":blog.private_public,})
      return jsonify(posts)
      # return jsonify({'total_posts':user.total_post,"followers": user.followers,'following':user.following,'email':user.email,"last_login":user.last_login,"username":user.username}),200
    except Exception as e:
      return make_response(e, 403)

  elif request.method == "DELETE":
    try:
      id = request.args['blog_id']
      blogpost.query.filter_by(posted_by=username).filter_by(id=id).delete()
      db.session.commit()
      user = User.query.filter_by(username=current_user.username).first()
      user.total_post -=1
      db.session.commit()
      # print(a)
      return jsonify({"delete":"success"})
    except Exception as e:
      print(e)
      return jsonify({"delete":"fail"})


@app.route('/createpost',methods=['POST'])
@auth_required('token')
def createpost():
  try:
    data = request.json
    title = data['title']
    description= data['description']
    posted_by = current_user.username
    links = data['links']
    private_public = data['private_public']
    # print("In createpost",private_public)
    post = blogpost(
                title=title,
                description=description,
                posted_on=datetime.datetime.now(),
                posted_by=posted_by,
                links=links,
                private_public=private_public)
    db.session.add(post)
    db.session.commit()
    user = User.query.filter_by(username=current_user.username).first()
    user.total_post +=1
    db.session.commit()
    return jsonify({'status':True}),200
  except Exception as e:
    return jsonify({'status':False,"error":e})


#______________________________MY POST END_____________________________





#_______________________FRIEND PAGE___________________________________


# gives followes and following list of particular user
# login required
@app.route('/getfriendslist',methods=['GET'])
@auth_required('token')
def getfriendslist():
  try:
    user_id = current_user.id
    user_follower =  Followers.query.filter_by(followers=user_id).all()
    user_following =  Followers.query.filter_by(following=user_id).all()
    user_username = User.query.all()
    
    user_follower_list= []
    user_following_list=[]
    for f in user_follower:
      for user in user_username:
        if user.id == f.following:
          user_following_list.append(user.username)
    # print("Following_list",user_following_list)

    for f in user_following:
      for user in user_username:
        if user.id == f.followers:
          user_follower_list.append(user.username)
    # print("Follower_list",user_follower_list)
  
    user_following_dict =[]
    for i in user_following_list:
      user_following_dict.append({"username":i,"following":False})
    
    user_followers_dict =[]
    two_way = list(set(user_follower_list).intersection(user_following_list))
    # print(two_way)
    for user in user_follower_list:
      if user in two_way:
        user_followers_dict.append({"username":user,"following":True})
      else:
        user_followers_dict.append({"username":user,"following":False})


    # print("Followers",user_followers_dict)
    return jsonify({"followers":user_followers_dict,"following":user_following_dict})
   
  except Exception as e:
    return make_response(e, 403)


@app.route('/follow_user',methods=['GET'])
@auth_required('token')
def follow_user():
  try:
    user_id = current_user.id
    follow_username = request.args['follow_username']
    # print(follow_username)
    follow_user =User.query.filter_by(username = follow_username).first()
    follow_user_id = follow_user.id
    follow_user.total_followers += 1
    db.session.commit()

    # print (follow_user_id)

    query = Followers(
      followers=user_id,
      following = follow_user_id,
      )
    db.session.add(query)
    db.session.commit()

    user = User.query.filter_by(id = user_id).first()
    user.total_following +=1
    db.session.commit()

    return jsonify({"added":"success"})
  except Exception as e:
    return make_response(e, 403)

  
#unfollows given user from the current_users following list
@app.route('/unfollow_user',methods=['GET'])
@auth_required('token')
def unfollow_user():
  try:
    print("IN UNFOLLOW USER")
    user_id = current_user.id
    unfollow_username = request.args['unfollow_username']
    unfollow_user = User.query.filter_by(username=unfollow_username).first()
    unfollow_user_id = unfollow_user.id
    unfollow_user.total_followers -= 1
    db.session.commit()
  
    Followers.query.filter_by(followers = user_id,following = unfollow_user_id).delete()
    db.session.commit()

    user = User.query.filter_by(id = user_id).first()
    user.total_following -=1
    db.session.commit()

   
    return jsonify({"followers":"user_followers","following":"user_following"})
  except Exception as e:
    return make_response(e, 403)


#_______________________FRIEND PAGE END___________________________________


if __name__=="__main__":
    app.run()