from flask import Flask
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
        item = {'name': name, 'price': 10.00}
        items.append(item)
        return item, 201 #this is for creating a new item
    
    
api.add_resource(Item, '/item/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)