# Employee Management

This is a backend project to handle employee data stored in the database.

## API Reference

#### Get all employee details

```http
  GET /display
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get particular employee detail

```http
  GET /display/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of employee |

#### Add employee details to database

```http
  POST /add
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `api_key`      | `string` | **Required**. Your API key |

#### Edit existing employee details

```http
  PUT /edit?email
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `api_key`      | `string` | **Required**. Your API key |
| `email`      | `string` | **Required**. Email of employee |

```http
  PUT /edit?id
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `api_key`      | `string` | **Required**. Your API key |
| `id`      | `string` | **Required**. Id of employee |

#### Delete employee record

```http
  DELETE /delete/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of employee |


#### add_employee()

Adds employee details to database

#### display_employee()

Displays all employee details

#### display_employee_id(id)

Displays employee details of employee with given id

#### update_employee()

Updates employee details based on email or id

#### delete_employee(id)

Deletes employee of employee with given id

#### not_found()

Displays error when values for all fields have not been entered

#### init()

Initialises field values to False to avoid keyerror

#### validate_all(firstname,lastname,contact,email)

Calls functions to validate firstname, lastname, contact and email

#### validate_name(name)

Validates firstname and lastname

#### validate_contact(num)

Validates contact number

#### validate_email(email)

Validates email id

#### error_message()

Concatenates error messages for failed validation

#### check_repeat(email,num)

Checks if email id or contact number has already been registered
