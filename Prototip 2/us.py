# Aquest client de consola fa el següent:
# Recull el username de l'usuari.
# Obté la informació de l'usuari pel seu username.

import requests

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def __str__(self):
        return f"[User] ID: {self.id}, Username: {self.username}, Email: {self.email}"


class Child:
    def __init__(self, id, name, sleep_average, treatment, time):
        self.id = id
        self.name = name
        self.sleep_average = sleep_average
        self.treatment = treatment
        self.time = time

    def __str__(self):
        return f"[Child] ID: {self.id}, Name: {self.name}, Sleep Avg: {self.sleep_average}, Treatment: {self.treatment}, Time: {self.time}h"


class APIClient:
    BASE_URL = "http://localhost:5000/prototip2"  

    @staticmethod
    def get_user(username):
        try:
            response = requests.get(f"{APIClient.BASE_URL}/getuser", params={"username": username})
            if response.status_code == 200:
                data = response.json()
                return User(data['id'], data['username'], data['email'])
            else:
                print(f"Error: {response.json().get('error', 'Usuari no trobat')}")
                return None
        except Exception as e:
            print(f"Connection Error: {e}")
            return None

    @staticmethod
    def get_children(username):
        try:
            response = requests.get(f"{APIClient.BASE_URL}/getchildren/{username}")
           
            if response.status_code == 200:
                children_data = response.json()
                return [Child(c["id"], c["name"], c["sleep_average"], c["treatment"], c["time"]) for c in children_data]
               
            else:
                print(f"Error: {response.json().get('error', 'No children found')}")
                return []
        except Exception as e:
            print(f"Connection Error: {e}")
            return []

class ConsoleView:
    @staticmethod
    def menu():
        print("\n--- MENU ---")
        print("1. Consultar Usuari")
        print("2. Consultar Nens de l'Usuari")
        print("3. Sortir")

    @staticmethod
    def run():
        while True:
            ConsoleView.menu()
            option = input("Selecciona una opció: ")

            if option == "1":
                username = input("Introdueix el nom d'usuari: ")
                user = APIClient.get_user(username)
                if user:
                    print(user)
            
            elif option == "2":
                username = input("Introdueix el nom d'usuari: ")
                children = APIClient.get_children(username)
                if children:
                    for child in children:
                        print(child)
                else:
                    print("Aquest usuari no té nens associats")

            elif option == "3":
                print("Adeu!")
                break

            else:
                print("Opció incorrecta. Torna a intentar-ho.")

if __name__ == "__main__":
    ConsoleView.run()