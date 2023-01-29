from flask import Flask, jsonify, request,make_response
from flask_cors import CORS
from flask_restful import Api, Resource
import os
from flask_sqlalchemy import SQLAlchemy
from models import *
import datetime
from flask_security import Security, SQLAlchemySessionUserDatastore, auth_required, hash_password,current_user
from config import LocalDevelopmentConfig



# current_dir = os.path.abspath(os.path.dirname(__file__))
# app.config['SECRET_KEY']= "123456"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(current_dir,"database.sqlite3")
# app.config['WTF_CSRF_ENABLED'] = False
# app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = "Authentication-Token"
# app.config['SECURITY_PASSWORD_SALT']="thisissecret"
app=None
# api=None
def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config.from_object(LocalDevelopmentConfig)
  db.init_app(app)
  app.app_context().push()
  user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
  security = Security(app, user_datastore)
  # api = Api(app)
  app.app_context().push()
  with app.app_context():
    db.create_all()
  # return app, api
  return app

# app,api = create_app()

app= create_app()

@app.route('/')
@auth_required('token')
def home():
  if current_user.is_authenticated:
    return current_user.email
  else:
    return "Login "


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
    followers = "" if user.followers == None else user.followers.split(',')
    following = "" if user.following == None else user.following.split(',')
    last_login = "" if user.last_login == None else user.last_login

    print(user.last_login)
    return jsonify({"profile":True,'total_posts':user.total_post,"followers": followers,'following':following,'email':user.email,"last_login":last_login,"username":user.username}),200
  except Exception as e:
    return jsonify({"profile":False})
  
# give out blogs of all following friend of given user
# login required

@app.route('/getblogs',methods=['GET'])
@auth_required('token')
def getblogs():
  try:
    username = current_user.username
    posts=[]
    user_following =  User.query.filter_by(username=username).first()
    user_following = user_following.following.split(',')
    print("user_foloowing",user_following)
    blogs = blogpost.query.all()
    for blog in blogs:
      if blog.posted_by in user_following:
        print(blog.title)
        posts.append({"title":blog.title,
                      "description":blog.description,
                      "posted_on":blog.posted_on,
                      "likes":blog.likes,
                      "posted_by":blog.posted_by,
                      "links":blog.links,
                      "imgurl":blog.imgurl,})
    return jsonify(posts)
    # return jsonify({'total_posts':user.total_post,"followers": user.followers,'following':user.following,'email':user.email,"last_login":user.last_login,"username":user.username}),200
  except Exception as e:
    return jsonify([])

    
# give out blogs of a particular user
# login required
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
                          "imgurl":blog.imgurl,})
      return jsonify(posts)
      # return jsonify({'total_posts':user.total_post,"followers": user.followers,'following':user.following,'email':user.email,"last_login":user.last_login,"username":user.username}),200
    except Exception as e:
      return make_response(e, 403)
  elif request.method == "DELETE":
    try:
      id = request.args['blog_id']
      blogpost.query.filter_by(posted_by=username,id=id).delete()
      db.session.commit()
      # print(a)
      return jsonify({"delete":"success"})
    except Exception as e:
      print(e)
      return jsonify({"delete":"fail"})


@app.route('/follow_user',methods=['GET'])
@auth_required('token')
def follow_user():
  try:
    username = current_user.username
    follow_username = request.args['follow_username']
    user =  User.query.filter_by(username=username).first()
    user.following += ","+follow_username
    db.session.commit()
    return jsonify({"added":"success"})
  except Exception as e:
    return make_response(e, 403)

# gives followes and following list of particular user
# login required
@app.route('/getfriendslist',methods=['GET'])
@auth_required('token')
def getfriendslist():
  try:
    username = current_user.username
    print(username)
    user =  User.query.filter_by(username=username).first()
    user_following = user.following.split(',')
    user_followers = user.followers.split(',')
   
    two_way = list(set(user_following).intersection(user_followers))
    print(two_way)
    user_followers_dict =[]
    for user in user_followers:
      if user in two_way:
        user_followers_dict.append({"username":user,"following":True})
      else:
        user_followers_dict.append({"username":user,"following":False})
    # return jsonify({"followers":user_followers[0:len(user_followers)-1],"following":user_following[0:len(user_following)-1]})
    return jsonify({"followers":user_followers_dict,"following":user_following})
 
  except Exception as e:
    return make_response(e, 403)
  
#unfollows given user from the current_users following list
@app.route('/unfollow_user',methods=['GET'])
@auth_required('token')
def unfollow_user():
  try:
    print("IN UNFOLLOW USER")
    username = current_user.username
    unfollow_username = request.args['unfollow_username']
    # print(username,unfollow_username)
    user =  User.query.filter_by(username=username).first()
    following_list = user.following.split(',')
    print(unfollow_username)
    new_following_list=""
    if following_list != []:
      following_list.remove(unfollow_username)
      print(following_list)
      for i in following_list:
        new_following_list += i+","
    
    print(new_following_list)

    user.following = new_following_list[0:len(new_following_list)-1]
    db.session.commit()
    # user_following = user.following.split(',')
    # user_followers = user.followers.split(',')
    # print(user_following,user_followers)
    return jsonify({"followers":"user_followers","following":"user_following"})
  except Exception as e:
    return make_response(e, 403)


#gives top 5 trending blogs 
# login NOT required 
@app.route('/gettrendingblogs',methods=['GET'])
def gettrendingblogs():
  try:
    posts=[]
    blogs = blogpost.query.order_by(blogpost.likes.desc()).limit(1)
    for blog in blogs:
      print(blog.title)
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



#blogs created by users 
# login required
@app.route('/createpost',methods=['POST'])
@auth_required('token')
def createpost():
  try:
    data = request.json
    title = data['title']
    description= data['description']
    posted_by = current_user.username
    links = data['links']
    # print(data)
    post = blogpost(
      title=title,
      description=description,
      posted_on=datetime.datetime.now(),
      posted_by=posted_by,
      links=links
      )
    db.session.add(post)
    db.session.commit()
    return jsonify({'token':"token"}),200
  except Exception as e:
    return make_response(e, 403)



if __name__=="__main__":
    app.run()