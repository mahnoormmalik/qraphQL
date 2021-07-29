""" app.py """
from flask import Flask
from flask_graphql import GraphQLView
from mongoengine import connect
import os

from schema import schema

DATABASE = 'flask-mongodb-graphene'
PASSWORD = os.environ.get("MONGODB_PASSWORD")

client = connect(DATABASE, host=f'mongodb+srv://mahnoor:{PASSWORD}@cluster0.cc5rd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', alias='default')

app = Flask(__name__)
app.debug = True

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(port=5002)