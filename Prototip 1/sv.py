from flask import Flask, request, jsonify
from dadesServer import users

app = Flask(__name__)

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
