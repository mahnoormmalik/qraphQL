import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from models import User as UserModel

class User(MongoengineObjectType):
    class Meta:
        description = "User"
        model = UserModel
        # interfaces = (Node,)

class Query(graphene.ObjectType):
    users = graphene.List(User)
    users_by_id = graphene.Field(User, name=graphene.String())
    
    def resolve_users(self, info):
        # print(info)
        return list(UserModel.objects.all())
    def resolve_users_by_id(self, info, name):
        return UserModel.objects.get(name=name)

schema = graphene.Schema(query=Query, types=[User])