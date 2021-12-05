from flask import Flask
from flask_restful import Resource, Api
import csv
from klasy import Filmy
from klasy import links
from klasy import oceny
from klasy import tags

app = Flask(__name__)
api = Api(app)



filmy: list = []

with open('movies.csv',  encoding="utf8",  newline='\n') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar="\"")
    header = next(data)
    for row in data:
        filmy.append(Filmy.Film(int(row[0]), row[1], row[2]))


class Movies(Resource):
    def get(self):
        return[f.__dict__ for f in filmy]


api.add_resource(Movies,'/movies', '/', endpoint='movies')


linklist: list = []

with open('links.csv',  encoding="utf8",  newline='\n') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar="\"")
    header = next(data)
    for row in data:
        linklist.append(links.Link(int(row[0]), row[1], row[2]))


class LinkLista(Resource):
    def get(self):
        return[l.__dict__ for l in linklist]


api.add_resource(LinkLista, '/links', '/', endpoint='links')


ocenylist: list = []

with open('ratings.csv',  encoding="utf8",  newline='\n') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar="\"")
    header = next(data)
    for row in data:
        ocenylist.append(oceny.Ocena(int(row[0]), row[1], row[2],row[3]))


class ratingslist(Resource):
    def get(self):
        return[o.__dict__ for o in ocenylist]


api.add_resource(ratingslist, '/ratings', '/', endpoint='ratings')


tagslist: list = []

with open('tags.csv',  encoding="utf8",  newline='\n') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar="\"")
    header = next(data)
    for row in data:
        tagslist.append(tags.Tag(int(row[0]),row[1], row[2],row[3]))


class taglist(Resource):
    def get(self):
        return[t.__dict__ for t in tagslist]


api.add_resource(taglist, '/tags', '/', endpoint='tags')

if __name__ == '__main__':
    app.run(debug=True)
