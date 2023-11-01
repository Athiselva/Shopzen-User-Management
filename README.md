
# Python - User Management API

This is a Flask-based RESTful API for managing user information with added security features for password hashing. The API provides endpoints for creating users, updating user information, fetching user details by ID, and fetching a list of all users. User passwords are securely hashed using the `bcrypt` library for enhanced security.

## Installation

Follow these steps to set up and run the Flask User Management API:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/flask-user-management-api.git
   cd flask-user-management-api

2. Install the required packages:

   ```bash
   pip install -r requirements.txt

3. Create a .env file in the project directory with the following content:

   ```bash
   SQLALCHEMY_DATABASE_URI=mysql://your_username:your_password@localhost/shopzen_user_management

4. Start the Flask application:
   <br>
   ```
   python user_management.py
   ```

5. Security
   <br><br>This API ensures password security by securely hashing user passwords using the bcrypt library. Passwords are never stored in plain text format, providing an added layer of security for user data.

6. Usage
    You can interact with the API using HTTP requests. Here are some examples using curl:

Create a new user:

 ```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com", "phone_number": "1234567890", "address": "123 Main St", "is_admin": false, "username": "johndoe", "password": "password123", "created_by": 1, "modified_by": 1}' http://localhost:8082/users

Update a user's username and password:

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"username": "newusername", "password": "newpassword123"}' http://localhost:8082/user/1

Fetch user information by ID:

```bash
curl http://localhost:8082/user/1

Fetch a list of all active users:

```bash
curl http://localhost:8082/users

Delete a user:

```bash
curl -X DELETE http://localhost:8082/user/1
