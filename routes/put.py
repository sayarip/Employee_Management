from bson.objectid import ObjectId
from flask import jsonify, request
import validate
from error import not_found
from res import field,init,mongo

def update_employee():
    init()
    try:
        _json = request.json
        field['_firstname']=_json['first_name']
        field['_lastname']=_json['last_name']
        field['_contact']=_json['contact']
        field['_email']=_json['email']
    except KeyError:
        print('Warning: Keys are missing')
    id=request.args.get('id')
    email=request.args.get('email')
    if field['_firstname'] and field['_lastname'] and field['_contact'] and field['_email']:
        if validate.validate_name(field['_firstname']) and validate.validate_name(field['_lastname']) and validate.validate_contact(field['_contact']) and validate.validate_email(field['_email']):
            if id or email:
                if mongo.db.employees.find_one({'email':email}) or mongo.db.employees.find_one({'email':email}) :
                    if validate.check_repeat(field['_email'],field['_contact'])==True:
                        if email:
                            mongo.db.employees.update_one({'email':email}, {'$set': {'first_name': field['_firstname'],'last_name': field['_lastname'],'contact':field['_contact'],'email':field['_email']}})        
                        if id:
                            mongo.db.employees.update_one( {'_id':ObjectId(id)} , {'$set': {'first_name': field['_firstname'],'last_name': field['_lastname'],'contact':field['_contact'],'email':field['_email']}})        
                        response=jsonify("User has been updated successfully")
                        response.status_code=200
                        return response
                    else:
                        return validate.check_repeat(field['_email'],field['_contact'])
                else:
                    response=jsonify("Employee not found")
                    response.status_code=404
                    return response
            else:
                response=jsonify("ID or Email id not provided.")
                return response
        else:
            return  validate.error_message()
    else:
        return not_found()