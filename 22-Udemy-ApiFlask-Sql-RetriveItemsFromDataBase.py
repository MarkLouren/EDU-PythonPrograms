####################################################################################################
###############################create_tables.py ######### 
###################################################################################################

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" #ID will be assigned automaticaly
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)
cursor.execute("INSERT INTO items VALUES ('test', 10.99)")
connection.commit()
connection.close()


####################################################################################################
###############################app.py ######### 
###################################################################################################
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'vova'
api = Api(app)
jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run (port = 3001, debug=True)


####################################################################################################
###############################item.py ######### 
###################################################################################################
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()  # instead of json to be sure that only price past in no other
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be left blank!")


    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor=connection.cursor()
        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        else:
            return {'message': 'Item not found'}, 404


    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists".format(name)}, 400
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201
        
####################################################################################################
###############################User.py ######### 
###################################################################################################
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
        result = cursor.execute (query, (_id,)) #username,)- show to python that we've created a tupple
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
        if User.find_by_usernsme(data['username']):  #help to avoid dublicate users, check if user=None than..put before connection, or it never close
            return {"message":"A user with that username already exists"},400
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)" #NUL: because id is auto incrementing
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()
        return {"message": "User was created sucessfully"}, 201
####################################################################################################
###############################Security.py ######### 
###################################################################################################
from user import User


def authenticate(username, password):  #authentication of a user
    user = User.find_by_usernsme(username)
    if user and user.password == password:  #check it
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
