from flask import Flask
from flask_restful import Resource, Api
import csv
from klasy import Filmy

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

filmy: list = []

with open('movies.csv', newline='\n') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar="\"")
    header=next(data)
    for row in data:
        filmy.append(Filmy.Film(int(row[0]), row[1], row[2]))


class Movies(Resource):
    def get(self):
        return[f.__dict__ for f in filmy]

api.add_resource(Movies, '/')

if __name__ == '__main__':
    app.run(debug=True)
