from flask import jsonify
import re
from werkzeug.wrappers import response
from res import mongo

message=" "

def validate_all(firstname,lastname,contact,email):
    global message
    message=" "
    valid_fname=validate_name(firstname)
    valid_lname=validate_name(lastname)
    valid_num=validate_contact(contact)
    valid_mail=validate_email(email)
    if valid_fname and valid_lname and valid_num and valid_mail:
        return True
    else:
        return False

def validate_name(name):
    global message
    if re.match('^[a-zA-Z. ]+$',name):
        return True
    else:
        response = 'Name can only consist of alphabets!'
        message= message+' '+response
        return False

def validate_contact(num):
    global message
    if re.match('^[0-9]+$',num) and len(num)==10:
        return True
    else:
        response = 'Contact number can only consist of digits from 0-9 and should be 10 digits long!'
        message= message+' '+response
        return False

def validate_email(email):
    global message
    if re.match('[\w.-]+@[\w.-]+\.com$',email):
        return True
    else:
        response = 'Email id should have @ and end with .com!'
        message= message+' '+response
        return False

def error_message():
    response=jsonify(message)
    response.status_code=400
    return response

def check_repeat(email,num):
    if mongo.db.employees.find_one({'email':email}) or mongo.db.employees.find_one({'contact':num}):
        response = jsonify('Email or contact number already registered!')
        response.status_code = 400
        return response
    else:
        return True

