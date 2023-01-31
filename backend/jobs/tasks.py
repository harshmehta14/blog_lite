from jobs.workers import celery
from datetime import datetime
from jobs.mail import send_email, write
from celery.schedules import crontab
import os 


#SENDING MAIL WITH BLOG DETAILS IN CSV FORMAT
@celery.task()
def send_blog_csv(username,email):
  job = send_email(email,subject=username+"'s Blog Posts", message = "Welcome to BlogLite \nPlease find the attached csv file of you Blogs \nThank You.", attachment_file='./static/'+username+"_blogs.csv")
  # dir_path = os.path.dirname(os.path.realpath(__file__))
  # print(dir_path)
  print("SENDING MAIL WITH CSV FILE")


@celery.on_after_configure.connect
def monthly_report(sender,**kwargs):
  sender.add_periodic_task(10.0,just_say_hello.s(), name='add every 10')
  # Calls test('world') every 30 seconds
  # sender.add_periodic_task(30.0, test.s('world'), expires=10)

  # # Executes every Monday morning at 7:30 a.m.
  # sender.add_periodic_task(
  #     crontab(hour=7, minute=30, day_of_week=1),
  #     test.s('Happy Mondays!'),
  #   )
  # sender.add_periodic_task(
  #       crontab(hour=21, minute=00, day_of_week="*"),
  #       just_say_hello.s(),
  #       name='daily'
  #        )

  


@celery.task()
def test():
  print("hello")

  # f = open("demofile2.txt", "w")
  # f.write("Now the file has more content!")
  # f.close()
  
  a = send_email("hema@bloglite.com",subject="Hi there, celery sent this", message = "Welcome to BlogLite")
  print(a)