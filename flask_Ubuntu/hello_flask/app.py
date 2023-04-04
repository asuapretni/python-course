from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)
    
    def __init__(self, title, content):    # def __init__(self, id, title, content): #to change id 
        self.title = title
        self.content = content
        # self.id = id    # to change id

class GuideSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content')


guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)


# to create the database from the python repl use. (the commands in the video not working)
# >>> from app import app, db
# >>> app.app_context().push()
# >>> db.create_all()


# endpoint to create a new guide
@app.route('/guide', methods=["POST"])
def add_guide():
    # id = request.json['id']  # to change the id
    title = request.json['title']
    content = request.json['content']

    new_guide = Guide(title, content)   # new_guide = Guide(id, title, content)

    db.session.add(new_guide)
    db.session.commit()

    
    #guide = Guide.query.get(new_guide.id)   #video version, next line updated version SQLAlchemy
    guide = db.session.get(Guide, new_guide.id)
    return guide_schema.jsonify(guide)

# Endpoint to query all guides
@app.route("/guides", methods=["GET"])
def get_guides():
    all_guides = Guide.query.all()
    result = guides_schema.dump(all_guides)
    return jsonify(result)  # In video -> return jsonify(result.data) not working, dump return data


# Endpoint for querying a single guide
@app.route("/guide/<id>", methods=["GET"])    # Note the <id> syntax, different from the other routes and methods  
def get_guide(id):
    guide = db.session.get(Guide, id)
    # guide = Guide.query.get(id)    #video version, previous line updated version SQLAlchemy
    return guide_schema.jsonify(guide)


# Endpoint for updating a guide
@app.route("/guide/<id>", methods=["PUT"])
def guide_update(id):
    guide = db.session.get(Guide, id)
    #guide = Guide.query.get(id)    #video version, previous line updated version SQLAlchemy
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

   # return guide_schema.jsonify(guide)   # this return the delete object
    return "Guide was successfully deleted"


if __name__ == '__main__':
    app.run(debug=True)


# to create the database from the python repl use. (the commands in the video not working)
# >>> from app import app, db
# >>> app.app_context().push()
# >>> db.create_all()


