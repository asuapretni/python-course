from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))  # this is the base directory whatever it will be
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)    # allow to create a database to develop porpouses only
ma = Marshmallow(app)   # allow to creaate the database Schema


class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):    # to change id see ubuntu version
        self.title = title
        self.content = content


class GuideSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content')


guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)


# Use this commands in python console to create the databese app.sqlite
# The commands in the video not working
# >>> from app import app, db
# >>> app.app_context().push()
# >>> db.create_all()


# Endpoint to create a new guide
@app.route('/guide', methods=["POST"])
def add_guide():
    title = request.json['title']
    content = request.json['content']

    new_guide = Guide(title, content)

    db.session.add(new_guide)
    db.session.commit()

    # guide = Guide.query.get(new_guide.id)    #video version, next line updated version SQLAlchemy
    guide = db.session.get(Guide, new_guide.id)

    return guide_schema.jsonify(guide)


# Endpoint to query all guides
@app.route("/guides", methods=["GET"])
def get_guides():
    all_guides = Guide.query.all()
    result = guides_schema.dump(all_guides)
    return jsonify(result)  # In video -> return jsonify(result.data) not working dump return data


# Endpoint for querying a single guide
@app.route("/guide/<id>", methods=["GET"])    # Note the <id> syntax, different from the other routes and methods
def get_guide(id):
    # guide = Guide.query.get(id)    #video version, next line updated version SQLAlchemy
    guide = db.session.get(Guide, id)
    return guide_schema.jsonify(guide)


# Endpoint for updating a guide
@app.route("/guide/<id>", methods=["PUT"])
def guide_update(id):
    # guide = Guide.query.get(id)    #video version, next line updated version SQLAlchemy
    guide = db.session.get(Guide, id)
    title = request.json['title']
    content = request.json['content']

    guide.title = title
    guide.content = content

    db.session.commit()
    return guide_schema.jsonify(guide)


# Endpoint for deleting a record
@app.route("/guide/<id>", methods=["DELETE"])
def guide_delete(id):
    guide = db.session.get(Guide, id)
    db.session.delete(guide)
    db.session.commit()

    # return guide_schema.jsonify(guide)  # This returns the deleted guide
    return "Guide was successfully deleted"


if __name__ == '__main__':
    app.run(debug=True)

# curl -X POST localhost:5000/guide -H "Content-Type: application/json" -d @app_post.json
# curl -X POST localhost:5000/guide -H "Content-Type: application/json" -d '{"content": "Some content", "title": "My first guide"}'
# curl -X PUT localhost:5000/guide/1 -H "Content-Type: application/json" -d '{"content": "Some  NEW content", "title": "My first guide"}'
