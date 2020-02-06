from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList


app = Flask(__name__)
#app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exceptions even if debug is set to false on app
app.secret_key = 'password'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth

# items = []

# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('price', type=float, required=True, help="you must put somethign in this field and DO NOT leave blank!")

#     @jwt_required()
#     def get(self, name):
#         return {'item': next(filter(lambda x: x['name'] == name, items), None)}
    
#     @jwt_required()
#     def post(self, name):
#         if next(filter(lambda x: x['name'] == name, items), None) is not None:
#             return {'message': "An item with the name '{}' already exists.".format(name)}

#         data = Item.parser.parse_args()

#         item = {'name': name, 'price': data['price']}
#         items.append(item)
#         return item

#     @jwt_required()
#     def delete(self, name):
#         global items
#         items = list(filter(lambda x: x['name'] != name, items))
#         return {'message': 'Item deleted'}

#     @jwt_required()
#     def put(self, name):
#         data = Item.parser.parse_args()
#         item = next(filter(lambda x: x['name'] == name, items), None)
#         if item is None:
#             item = {'name': name, 'price': data['price']}
#             items.append(item)
#         else:
#             item.update(data)
#         return item

# class ItemList(Resource):
    # @jwt_required()
    # def get(self):
    #     return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)