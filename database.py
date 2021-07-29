import json
# from jsonpath import jsonpath
from mongoengine import connect
import os

from models import User

DATABASE = "flask-mongodb-graphene"
PASSWORD = os.environ.get("MONGODB_PASSWORD")

client = connect(
    DATABASE,
    host=f"mongodb+srv://mahnoor:{PASSWORD}@cluster0.cc5rd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    alias="default",
)
client.drop_database(DATABASE)


def init_db():

    with open("data.json", "r") as file:
        data = json.loads(file.read())
        for elem in data["users"]:
            user = User(name=elem["name"], email= elem["email"], age=elem["age"])
            user.save()
            # print(elem)

if __name__ == "__main__":
    init_db()