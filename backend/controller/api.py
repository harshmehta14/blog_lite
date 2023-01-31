from flask_restful import Resource, marshal_with, fields
from data.models import *
from flask_security import auth_required


output_fields= {
    "user_id":fields.Integer,
    "username":fields.String,
    "email":fields.String
}

class UserAPI(Resource):
    # @marshal_with(output_fields)
    @auth_required("token")
    def get(self,username):
        user = User.query.filter_by(username=username).first()
        return ({"user_id":user.id})

    def put(self):
        pass

    def delete(self):
        pass
    def update(self):
        pass


class BlogPostAPI(Resource):
    # @marshal_with(output_fields)
    @auth_required("token")
    def get(self,username):
        user = User.query.filter_by(username=username).first()
        return ({"user_id":user.id})

    def post(self):
        username

    def delete(self):
        pass
    def update(self):
        pass

    
