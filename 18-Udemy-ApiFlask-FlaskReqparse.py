from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


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

app.run (port = 3001, debug=True)
