""" models.py """
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField,
    ListField,
    ReferenceField,
    StringField,
    IntField,
)

class User(Document):
    meta = {"collection": "user"}
    name = StringField()
    email = StringField()
    age = IntField()
