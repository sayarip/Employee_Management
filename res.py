from flask import Flask
from flask_pymongo import PyMongo

app= Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Employee"
mongo = PyMongo(app)

field={
    '_firstname':False,
    '_lastname':False,
    '_contact':False,
    '_email':False
}

def init():
    for key in field:
        field[key]=False


