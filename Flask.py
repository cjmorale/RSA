from flask import Flask, jsonify, abort, request, render_template
from flask_sqlalchemy import SQLAlchemy
from RSA import *

app = Flask(__name__)
app.config.from_pyfile('Config.py')
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    modulas = db.Column(db.String(5000))
    exponent = db.Column(db.String(5000))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, modulas, exponent, email):
        self.name = name
        self.modulas = modulas
        self.exponent = exponent
        self.email = email


@app.route('/dev/', methods=['GET'])
def index():
    x = Users.query.all()
    print(x)

    return jsonify({'Users': 'hello'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
