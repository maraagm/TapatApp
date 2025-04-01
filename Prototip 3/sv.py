import dadesServer as server
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/prototip2/login", methods=["POST"])
def login():
    try:
        data = request.json  
        username = data.get("username")
        password = data.get("password")

        user = server.DAOUser.getUserByCredentials(username, password)

        if user:
            token = server.DAOUser.generate_token(username)
            return jsonify({"id": user.id, "username": user.username, "email": user.email, "token": token}), 200
        else:
            return jsonify({"error": "Credenciales incorrectas"}), 401
    except Exception as e:
        return jsonify({"error": "Error inesperado del sistema", "detalles": str(e)}), 500

@app.route("/prototip2/children/<int:user_id>", methods=["GET"])
def getChildrenByUser(user_id):
    try:
        children = server.DAOChild.getChildrenByUser(user_id)

        if children:
            return jsonify([child.__dict__ for child in children]), 200
        else:
            return jsonify({"error": "Este usuario no tiene niños asociados"}), 404
    except Exception as e:
        return jsonify({"error": "Error inesperado del sistema", "detalles": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=10050)