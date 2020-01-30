from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
   #@app.route('/student/<string:name>') # we do not need to this step here since we are calling the resources using our api call!!
    def get(self, name):
        return {'student:': name}
    

api.add_resource(Student, '/student/<string:name>') 
# this is used to access the student resource at http://127.0.0.1:5000/student/name

if __name__ == '__main__':
    app.run(debug=True)