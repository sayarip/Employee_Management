from flask import jsonify, request
import validate
from error import not_found
from res import field,init,mongo

def add_employee():
    init()
    try:
        _json = request.json
        field['_firstname']=_json['first_name']
        field['_lastname']=_json['last_name']
        field['_contact']=_json['contact']
        field['_email']=_json['email']
    except KeyError:
        print('Warning: Keys are missing')

	# validate the received values
    if field['_firstname'] and field['_lastname'] and field['_contact'] and field['_email']:
        if validate.validate_all(field['_firstname'],field['_lastname'],field['_contact'],field['_email']):
            # save details
            if validate.check_repeat(field['_email'],field['_contact'])==True:
                id = mongo.db.employees.insert({'first_name': field['_firstname'],'last_name': field['_lastname'],'contact':field['_contact'], 'email': field['_email']})
                response = jsonify('User added successfully!')
                response.status_code = 200
                return response
            else:
                return validate.check_repeat(field['_email'],field['_contact'])
        else:
            return  validate.error_message()
    else:
        return not_found()



