import hashlib
import uuid

# Clase User 
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email

users = [
    User(id=1, username="mare", password="123", email="mare@gmail.com"),
    User(id=2, username="pare", password="12", email="pare@gmail.com")
]

# Relación entre usuarios y niños
relation_user_child = [
    {"user_id": 1, "child_id": 1, "rol_id": 1},
    {"user_id": 1, "child_id": 3, "rol_id": 2},
    {"user_id": 2, "child_id": 2, "rol_id": 1}
]

class Child: 
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

children = [
    Child(id=1, child_name="Carla Montes", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Jose Perez", sleep_average=10, treatment_id=2, time=6),
    Child(id=3, child_name="Daniel Montes", sleep_average=6, treatment_id=1, time=5)
]

# Diccionario para almacenar tokens activos
active_tokens = {}

# ---- DAO Classes ----
class DAO_User:
    def __init__(self):
        self.listUsers = users

    def getUserByCredentials(self, username, password):
        for user in self.listUsers:
            if username == user.username and password == user.password:
                return user
        return None

    def generate_token(self, username):
        if username in active_tokens:
            return active_tokens[username]  # Devuelve el token existente
        
        salt = uuid.uuid4().hex
        token = hashlib.sha256((username + salt).encode()).hexdigest()
        active_tokens[username] = token  # Guarda el token en el diccionario
        return token

class DAO_Child:
    def __init__(self):
        self.listChildren = children
        self.relation_user_child = relation_user_child

    def getChildrenByUser(self, user_id):
        user_children_ids = [relation["child_id"] for relation in self.relation_user_child if relation["user_id"] == user_id]
        children_data = [child for child in self.listChildren if child.id in user_children_ids]
        return children_data if children_data else None

DAOUser = DAO_User()
DAOChild = DAO_Child()