from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404 
        # implement this step after explaining why we need to do it
        # and that is when we need to indicate that if an item does not exist, we want to return that 'null' value as a valid json dictionarry responce

    def post(self, name):
        data = request.get_json() 
        # putting 'force=True" if you are not sure if the client does not gives you a json file and another method is silent=True
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 #this is for creating a new item
    

class ItemList(Resource):
    def get(self):
        return {'items': items}    

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(debug=True)