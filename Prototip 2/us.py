import requests

# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return f"Id: {self.id}, Username: {self.username}, Password: {self.password}, Email: {self.email}"

class UserDAO:
    def get_user_by_username(username):
        response = requests.get(f'http://localhost:10050/prototip1/getuser?username={username}')
        if response.status_code == 200:
            user_data = response.json()
            user = User(user_data['id'], user_data['username'], user_data['password'], user_data['email'])
            return user
        else:
            return None
        
class ViewConsole:
    def getInputUsername():
        return input("Enter username: ")
    
    def showUserInfo(username):
        user = UserDAO.get_user_by_username(username)
        if user:
            print(f"User Info: {user}")
        else:
            print(f"User with username {username} not found")

if __name__ == "__main__":
    username = ViewConsole.getInputUsername()
    ViewConsole.showUserInfo(username)

#PROTOTIP 2
#LogIn 
    import requests

def login():
    username = input("Usuari: ")
    password = input("Password: ")

    data = {"username": username, "password": password}
    response = requests.post("http://127.0.0.1:5000/login", json=data)

    if response.status_code == 200:
        print("Login exitos!")
    else:
        print("Usuari o password incorrectes")

if __name__ == "__main__":
    login()
