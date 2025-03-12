from flask import Flask, request, jsonify
import dadesServer as dades

class DAOUsers:
    def __init__(self):
        self.users=dades.users
    def getUserByUsername(self,username):
        for u in self.users:
            if u.username == username:
                return u.__dict__
        return None

class DAORoles:
    def __init__(self):
        self.roles = dades.roles
    def getRolById(self, rol_id):
        for rol in self.roles:
            if rol.id == rol_id:
                return rol.type_rol
        return None
   
class DAOChild:
    def __init__(self):
        self.children = dades.children
        self.relations = dades.relation_user_child
        self.treatments = dades.treatments

    def getChildrenByUserId(self, user_id):
        result = []
        allowed_roles = [1, 2, 3]  # comprovació de rols

        for relation in self.relations:
            #if relation["user_id"] == user_id and relation["rol_id"] in allowed_roles:
            if relation.user_id == user_id and relation.rol_id in allowed_roles:
                for child in self.children:
                    if child.id == relation.child_id: #["child_id"]
                        treatment = self.getTreatmentById(child.treatment_id)
                        result.append({
                            "id": child.id,
                            "name": child.child_name,
                            "sleep_average": child.sleep_average,
                            "treatment": treatment.name if treatment else "Cap tractament",
                            "time": child.time
                        })
        return result

    def getTreatmentById(self, treatment_id):
        for treatment in self.treatments:
            if treatment.id == treatment_id:
                return treatment
        return None


app = Flask(__name__)
daoChild = DAOChild()
daoUser = DAOUsers()


@app.route('/prototip2/getuser/', methods=['GET'])
def get_user():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "No s'ha proporcionat cap nom d'usuari"}), 400

    user = daoUser.getUserByUsername(username)
    if user: #if existeix
        return jsonify({
            "id": user["id"],
            "username": user["username"],
            "email": user["email"]
        }), 200
    else:
        return jsonify({"error": "Usuari no trobat..."}), 404


@app.route('/prototip2/getchildren/<username>', methods=['GET'])
def get_children(username):
    user = daoUser.getUserByUsername(username)
    if not user:
        return jsonify({"error": "Usuari no trobat..."}), 404

    children = daoChild.getChildrenByUserId(user["id"]) if isinstance(user, dict) else daoChild.getChildrenByUserId(user.id)

    if children:
        return jsonify(children), 200  
    else:
        return jsonify({"error": "Aquest usuari no té nens associats"}), 404


#if __name__ == '__main__':
#    app.run(debug=True) 


user = daoUser.getUserByUsername("usuari1")
children = daoChild.getChildrenByUserId(user["id"]) if isinstance(user, dict) else daoChild.getChildrenByUserId(user.id)
print("aaa", children)