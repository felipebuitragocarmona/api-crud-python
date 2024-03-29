


from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

mysqlConnection = mysql.connector.connect(
    host="localhost",
    user="felibuca",
    password="felibuca",
    database="project_db"
)
cursor = mysqlConnection.cursor(dictionary=True)

@app.route('/', methods=['GET'])
def helloWorld():
    response={
        "message":"hello world"
    }
    return jsonify(response)

@app.route('/users', methods=['GET'])
def getUsers():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def createUser():
    data = request.get_json()
    name = data['name']
    password = data['password']
    email = data['email']
    nickname = data['nickname']
    cursor.execute("INSERT INTO users (name, password, email, nickname) VALUES (%s, %s, %s, %s)",
    (name, password, email, nickname))
    mysqlConnection.commit()
    return jsonify({"message": "User created successfully"})

@app.route('/users/<int:userId>', methods=['GET'])
def getUser(userId):
    cursor.execute("SELECT * FROM users WHERE id = %s", (userId,))
    user = cursor.fetchone()
    return jsonify(user)

@app.route('/users/<int:userId>', methods=['PUT'])
def updateUser(userId):
    data = request.get_json()
    name = data['name']
    password = data['password']
    email = data['email']
    nickname = data['nickname']
    cursor.execute("UPDATE users SET name = %s, password = %s, email = %s, nickname = %s WHERE id = %s",
    (name, password, email, nickname, userId))
    mysqlConnection.commit()
    return jsonify({"message": "User updated successfully"})

@app.route('/users/<int:userId>', methods=['DELETE'])
def deleteUser(userId):
    cursor.execute("DELETE FROM users WHERE id = %s", (userId,))
    mysqlConnection.commit()
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    print("hola mundo")
    app.run(debug=True)