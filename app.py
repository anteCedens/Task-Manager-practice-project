import os
from os import path
from flask import Flask
from flask_pymongo import Pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

if path.exists('env.py'):
    import env

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')


@app.route('/')
def hello():
    return 'Hello Flask - and Heroku!!'


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
