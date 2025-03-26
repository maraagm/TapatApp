import requests

class DAOUser:
    @staticmethod
    def getUserByCredentials(username, password):
        response = requests.post("http://localhost:10050/prototip2/login", json={"username": username, "password": password})

        if response.status_code == 200:
            userData = response.json()
            return userData  # Devuelve un diccionario con ID, username, email y token
        else:
            return None

class LoginView: 
    @staticmethod
    def getCredentials():
        username = input("Introduce tu username: ")
        password = input("Introduce tu password: ")
        return username, password

    @staticmethod
    def showUserInfo(username, password):
        user = DAOUser.getUserByCredentials(username, password)
        if user:
            print("\n✅ Inicio de sesión correcto!")
            print(" --- User Info --- ")
            print(f"ID: {user['id']}")
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print(f"Token: {user['token']}\n")
            return user
        else:
            print("❌ ERROR: Credenciales incorrectas\n")
            return None

class DAOChild:
    @staticmethod
    def getChildren(user_id, token):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"http://localhost:10050/prototip2/children/{user_id}", headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None

class ChildrenView:
    @staticmethod
    def showChildInfo(user_id, token):
        children = DAOChild.getChildren(user_id, token)
        if children:
            print("\n👶 --- Children Info --- ")
            for child in children:
                print(f"ID: {child['id']}")
                print(f"Nombre: {child['child_name']}")
                print(f"Promedio de sueño: {child['sleep_average']} horas")
                print()
        else:
            print("❌ ERROR: No hay niños asociados a este usuario.\n")

# ---- MAIN ----
if __name__ == "__main__":
    username, password = LoginView.getCredentials()
    user = LoginView.showUserInfo(username, password)

    if user:
        user_id = user["id"]
        token = user["token"]
        ChildrenView.showChildInfo(user_id, token)
    else:
        exit()