from flask import Flask, jsonify, request

app = Flask(__name__)

class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        print(self.username+":"+self.password+":"+self.email)

users = [
    User(id=1, username="usuari1", password="mare", email="mare@gmail.com"),
    User(id=2, username="usuari2", password="pare", email="pare@gmail.com")
]

class UserDAO:
    def __init__(self):
        self.users = users

    def get_all_users(self):
        result = []
        for user in self.users:
            result.append(user.__dict__)
        return result

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None

user_dao = UserDAO()

@app.route('/prototip1/users', methods=['GET'])
def get_users():
    return jsonify(user_dao.get_all_users())

@app.route('/prototip1/getuser', methods=['GET'])
def get_user_by_username():
    username=request.args.get('username', default="", type=str)
    print("+"+username+"+")
    user = user_dao.get_user_by_username(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": f"User with username {username} not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10050, debug=True)

#LogIn
    from flask import Flask, request, jsonify
from dadesServer import users

app = Flask(__name__)

#Verificar l'usuari
from dadesServer import users  

def verificar_usuario(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return True
    return False

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if verificar_usuario(username, password):
        return jsonify({"message": "Login exitoso", "status": "ok"}), 200
    else:
        return jsonify({"message": "Usuario o contraseña incorrectos", "status": "error"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
