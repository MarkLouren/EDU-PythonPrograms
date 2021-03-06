## app.py ####

from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
app = Flask(__name__)
app.secret_key = 'vova'
api = Api(app)
jwt = JWT(app, authenticate, identity) # /auth

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) #lambda function filter
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists".format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete (self, name):  #delete item
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put (self, name):  #change item
        data = request.get_json()
        item = next (filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item



class ItemList(Resource):
    def get(self):
        return  {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run (port = 3001, debug=True)

## security.py ################################################################

from user import User


users = [
   User (1,'bob', 'asdf')
]
username_mapping = {u.username: u for u in users} #retrive users by username
userid_mapping = {u.id: u for u in users} #retrive users by name


def authenticate(username, password):  #authentication of a user
    user = username_mapping.get(username, None) #retrive a user's name
    if user and user.password == password:  #check it
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)


## user.py ################################################################

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
