import os
from flask import Flask
from flask_pymongo import Pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'task_manager'
app.config['MONGO_URI'] = 'mongodb+srv://root:<password>@cluster0.6aiov.mongodb.net/<dbname>?retryWrites=true&w=majority'


@app.route('/')
def hello():
    return 'Hello Flask - and Heroku!!'


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
