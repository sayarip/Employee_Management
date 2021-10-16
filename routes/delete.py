from bson.objectid import ObjectId
from flask import jsonify
from res import mongo

def delete_employee(id):
    if mongo.db.employees.find_one({'_id':ObjectId(id)}):
        mongo.db.employees.delete_one({'_id':ObjectId(id)})
        response=jsonify("User has been deleted successfully")
        response.status_code=200
        return response
    else:
        response=jsonify("Employee with given id not found")
        response.status_code=404
        return response