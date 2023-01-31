import os
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from data.models import *
import datetime
from flask_security import Security, SQLAlchemySessionUserDatastore, hash_password, auth_required, current_user
from config import LocalDevelopmentConfig

from jobs.mail import send_email
from jobs import workers
from jobs import tasks
import pandas as pd
from requests_toolbelt.multipart import decoder

app=None
api=None
celery = None

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

  celery = workers.celery
  celery.conf.update(
    broker_url = app.config["CELERY_BROKER_URL"],
    result_backend= app.config["CELERY_RESULT_BACKEND"] 
  )
  celery.Task = workers.ContextTask
  app.app_context().push()
  with app.app_context():
    db.create_all()
  return app, api,celery
  # return app

app,api,celery = create_app()

from controller.api import *
api.add_resource(UserAPI,"/api/user","/api/user/<username>")


@app.route("/sendemail",methods=["GET"])
def sendemail():
  
  a = send_email("test@bloglite.com",subject="Hi there", message = "Welcome to BlogLite")
  
  return str(a),200


# celery -A main.celery worker -l info   /// TO RUN CELERY WORKERS
# celery -A main.celery beat --max-interval 1 -l info

   
   

  
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


#______________________ EMAIL-BLOGS CELERY-USER-TRIGGERED________________

@app.route("/send_blogcsv",methods=["GET"])
@auth_required('token')
def send_blogcsv():
  try:
    user_email = current_user.email
    user_name =  current_user.username
    user_blogs = blogpost.query.filter_by(posted_by = user_name).all()

    title_list=[]
    description_list=[]
    posted_on_list=[]
    imgurl_list=[]
    like_list=[]
    private_list=[]
    links_list=[]
    for blog in user_blogs:
      title_list.append(blog.title)
      description_list.append(blog.description)
      posted_on_list.append(blog.posted_on)
      imgurl_list.append(blog.imgurl)
      like_list.append(blog.likes)
      private_list.append(blog.private_public)
      links_list.append(blog.links)

    dict = {'Title': title_list, 'Description':description_list , 'posted_on':posted_on_list ,'imgurl':imgurl_list,"like":like_list,"Private":private_list,"links":links_list} 
    df = pd.DataFrame(dict)
    df.to_csv('./static/'+user_name+"_blogs.csv", encoding='utf-8')

    tasks.send_blog_csv(user_name,user_email)
    # job = tasks.send_blog_csv.apply_async((user_name,user_email),countdown = 10)
    # result = job.get()
    # print(result)
    return ({"status":"An email has been sent to your registered email with all your Blog Details"})
  except Exception as e:
    return ({"status":"Failed to Send email, try again later"})

#______________________ EMAIL-BLOGS CELERY-USER-TRIGGERED END________________





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
    return jsonify({"profile":True,'followers':user.total_followers,'following':user.total_following,'total_posts':user.total_post,'email':user.email,"last_login":last_login,"username":user.username}),200
  except Exception as e:
    return jsonify({"profile":False})
  
# give out blogs of all following friend of given user
# login required

#_____________________MY PROFILE END _________________________

  

#______________________________USER PROFILE_________________________________________

@app.route('/userprofile',methods=['GET'])
@auth_required('token')
def userprofile():
  try:
    username_profile =request.args['username']
    user = User.query.filter_by(username= username_profile).first()
    
    user_posts = blogpost.query.filter_by(posted_by=username_profile).all()
    print(user)
    posts=[]
    for blog in user_posts:
      if blog.private_public == 0:
        posts.append({"blog_id":blog.id,
                      "title":blog.title,
                      "description":blog.description,
                      "posted_on":blog.posted_on,
                      "likes":blog.likes,
                      "posted_by":blog.posted_by,
                      "links":blog.links,})

    return jsonify({"posts":posts,"profile":True,'followers':user.total_followers,'following':user.total_following,'total_posts':user.total_post}),200
  except Exception as e:
    return jsonify({"profile":False})



#______________________________USER PROFILE END_________________________________________



#_________________SEARCH RESULTS____________________


@app.route('/search_user',methods=['GET'])
@auth_required('token')
def search_user():
  try:
    user_id = current_user.id
    # user_follower =  Followers.query.filter_by(followers=user_id).all()
    user_following =  Followers.query.filter_by(followers=user_id).all()

    username_like = request.args['username']
    username_list = User.query.filter(User.username.like(username_like+"%")).all()
    # print(username_list)
    
    user_following_list=[]
    for f in user_following:
      user_following_list.append(f.following)
    # print("Follower_list",user_following_list)
  
    user_following_dict =[]
    for i in username_list:
      if i.id in user_following_list and i.id!=user_id:
        user_following_dict.append({"username":i.username,"following":True})
      elif i.id!=user_id:
        user_following_dict.append({"username":i.username,"following":False})
    
    print(user_following_dict)
    # user_followers_dict =[]
    # two_way = list(set(user_follower_list).intersection(user_following_list))
    # # print(two_way)
    # for user in user_follower_list:
    #   if user in two_way:
    #     user_followers_dict.append({"username":user,"following":True})
    #   else:
    #     user_followers_dict.append({"username":user,"following":False})


    # print("Followers",user_followers_dict)
    return jsonify(user_following_dict)
   
  except Exception as e:
    return make_response(e, 403)


#_________________SEARCH RESULTS END ____________________




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
    username = current_user.username
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
    return ({"posts":posts,"username":username})
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
    return jsonify({"posts":posts})
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







#__________________USERS POST_______________________

@app.route('/editblogdata',methods=['GET'])
@auth_required('token')
def editblogdata():
  try:
    id = request.args['id']
    blog = blogpost.query.filter_by(id = id).first()
    print(id)
    return jsonify({"title":blog.title,
                    "description":blog.description,
                    "links":blog.links,
                    "private_public":blog.private_public})
  except Exception as e:
      return make_response(e, 403)


@app.route('/updatepost',methods=['POST'])
@auth_required('token')
def updatepost():
  try:
    data = request.json
    title = data['title']
    description= data['description']
    posted_by = current_user.username
    links = data['links']
    private_public = data['private_public']
    blog_id = data['blog_id']

    blog = blogpost.query.filter_by(id =blog_id).first()
    blog.title = title
    blog.description = description
    blog.links = links
    blog.private_public = private_public
    db.session.commit()
    return jsonify({"status":True})
  except Exception as e:
    return jsonify({"status":False,"error":e})
  


      
#__________________USERS POST END_______________________



#________________________________MY POST ____________________________________________


    
# give out blogs of a particular user
@app.route('/crud_user_post',methods=['GET','DELETE',"POST"])
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
  
  elif request.method =="POST":
    try:
      data = request.json
      title = data['title']
      description= data['description']
      posted_by = current_user.username
      links = data['links']
      private_public = data['private_public']
      blog_id = data['blog_id']
      
      # post = blogpost(
      #             title=title,
      #             description=description,
      #             posted_on=datetime.datetime.now(),
      #             posted_by=posted_by,
      #             links=links,
      #             private_public=private_public)
      blog_updated = blogpost.query.filter_by(id=blog_id).update(dict(title=title,
                                                                  description=description,
                                                                  posted_on=datetime.datetime.now(),
                                                                  posted_by=posted_by,
                                                                  links=links,
                                                                  private_public=private_public))
      
      db.session.commit()
      user = User.query.filter_by(username=current_user.username).first()
      user.total_post +=1
      db.session.commit()
      return jsonify({'status':True}),200
    except Exception as e:
      return jsonify({'status':False,"error":e})




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
    # print(data['file'])
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

@app.route("/getchartdata",methods=['GET',"POST"])
def getchartdata():
  username = current_user.username
  print(username)
  user_post = blogpost.query.filter_by(posted_by=username).all()
  last_five_days =[0,0,0,0,0]
  name_five_days=[]

  for post in user_post:
    d=post.posted_on
    
  date_today = datetime.datetime.now() 
  for i in range (0,5):
    tom = date_today - datetime.timedelta(days=i)
    name_five_days.append(tom.strftime('%A'))
  
  print(name_five_days[::-1])
  
  return ({"label":name_five_days,'data':last_five_days})


if __name__=="__main__":
    app.run()