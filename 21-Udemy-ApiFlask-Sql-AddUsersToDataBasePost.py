####################################################################################################
###############################create_tables.py ######### create a new data base
####################################################################################################
import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" #ID will be assigned automaticaly
cursor.execute(create_table)
connection.commit()
connection.close()

####################################################################################################
###############################user.py ######### 
####################################################################################################

import sqlite3
from flask_restful import Resource,reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    @classmethod
    def find_by_usernsme(cls,username):  #cls - current class
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username =?"
        result = cursor.execute (query, (username,)) #username,)- show to python that we've created a tupple
        row =result.fetchone()
        if row:
            user = cls(*row) #the same as (row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls,_id):  #cls - current class
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id =?"
        result = cursor.execute (query, (_id,)) #_id,)- show to python that we've created a tupple
        row =result.fetchone()
        if row:
            user = cls(*row) #the same as (row[0], row[1], row[2])
        else:
            user = None
        connection.close()
        return user
class UserRegister(Resource):
#method should addd new users to db
    parser=reqparse.RequestParser()  #Parse the Json request check username and password
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="this field cannot be blank")

    parser.add_argument('password',
                    type=str,
                    required=True,
                    help="this field cannot be blank")
    def post (self):
        data=UserRegister.parser.parse_args()  #get data from the parser
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)" #NUL: because id is auto incrementing
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()
        return {"message": "User was created sucessfully"}, 201
        
  
####################################################################################################
###############################security.py ######### 
####################################################################################################
from user import User
def authenticate(username, password):  #authentication of a user
    user = User.find_by_usernsme(username)
    if user and user.password == password:  #check it
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
    
 ####################################################################################################
###############################app.py ######### 
####################################################################################################

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister


app = Flask(__name__)
app.secret_key = 'vova'
api = Api(app)
jwt = JWT(app, authenticate, identity) # /auth

items = []

class Item(Resource):
    parser = reqparse.RequestParser()  # instead of json to be sure that only price past in no other
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be left blank!")


    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) #lambda function filter
        return {'item': item}, 200 if item else 404

    def post(self, name):



        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete (self, name):  #delete item
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put (self, name):  #change item
        data = Item.parser.parse_args()
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
api.add_resource(UserRegister, '/register')

app.run (port = 3001, debug=True)
