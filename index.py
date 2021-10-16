from res import app
import routes.get as display
import routes.post as add
import routes.put as edit
import routes.delete as delete



#Adding employees
@app.route('/add', methods=['POST'])
def add_employee():
    return add.add_employee()

#Display all employees
@app.route('/display')
def display_employee():
    return display.display_employees()

#Display employees based on id
@app.route('/display/<id>')
def display_employee_id(id):
    return display.display_employee_id(id)

#Edit employee based on id or email
@app.route('/edit',methods=['PUT'])
def update_employee():
    return edit.update_employee()

#Delete an employee
@app.route('/delete/<id>',methods=['DELETE'])
def delete_employee(id):
    return delete.delete_employee(id)



if __name__=='__main__':
    app.run(debug=True)
