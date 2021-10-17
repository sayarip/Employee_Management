from res import app
from flask import jsonify

@app.errorhandler(404)
def not_found():
    response=jsonify("All fields have not been entered")
    response.status_code=404
    return response
