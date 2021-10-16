from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify
from res import mongo

def display_employees():
    employees=mongo.db.employees.find()
    response=dumps(employees)
    return response

def display_employee_id(id):
    if mongo.db.employees.find_one({'_id':ObjectId(id)}):
        employee=mongo.db.employees.find_one({'_id':ObjectId(id)})
        response=dumps(employee)
        print(response)
        return response
    else:
        response=jsonify("Employee with given id not found")
        response.status_code=404
        return response
    
