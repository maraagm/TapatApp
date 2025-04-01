import requests
import tkinter as tk
from tkinter import messagebox

class DAOUser:
    @staticmethod
    def getUserByCredentials(username, password):
        response = requests.post("http://localhost:10050/prototip2/login", json={"username": username, "password": password})

        if response.status_code == 200:
            userData = response.json()
            return userData  # Devuelve un diccionario con ID, username, email y token
        else:
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

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login App")
        self.root.geometry("400x300")  # Tamaño inicial de la ventana

        # Crear los widgets de la pantalla de inicio de sesión
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=20)

        # Área de texto para mostrar la información del usuario y los niños
        self.info_text = tk.Text(root, height=15, width=50, state="disabled")
        self.info_text.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Por favor, introduce username y password.")
            return

        user = DAOUser.getUserByCredentials(username, password)
        if user:
            self.display_user_info(user)
            self.get_children_info(user)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    def display_user_info(self, user):
        self.info_text.config(state="normal")
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, "✅ Inicio de sesión correcto!\n")
        self.info_text.insert(tk.END, " --- User Info --- \n")
        self.info_text.insert(tk.END, f"ID: {user['id']}\n")
        self.info_text.insert(tk.END, f"Username: {user['username']}\n")
        self.info_text.insert(tk.END, f"Email: {user['email']}\n")
        self.info_text.insert(tk.END, f"Token: {user['token']}\n")
        self.info_text.config(state="disabled")

    def get_children_info(self, user):
        user_id = user['id']
        token = user['token']
        children = DAOChild.getChildren(user_id, token)

        self.info_text.config(state="normal")
        if children:
            self.info_text.insert(tk.END, "\n👶 --- Children Info --- \n")
            for child in children:
                self.info_text.insert(tk.END, f"ID: {child['id']}\n")
                self.info_text.insert(tk.END, f"Nombre: {child['child_name']}\n")
                self.info_text.insert(tk.END, f"Promedio de sueño: {child['sleep_average']} horas\n\n")
        else:
            self.info_text.insert(tk.END, "\n❌ ERROR: No hay niños asociados a este usuario.\n")
        self.info_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()