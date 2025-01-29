# Definició dels EndPoints del Servei Web:

| Descripció | Host | End-point | Method | Tipus de petició | Parametres | 
|--------------|--------------|--------------|--------------|--------------|--------------|
| Servei que consulta un User per Username | 192.168.144.131:10050 | http://192.168.144.131:10050/tapatapp/getuser | GET | HTTP GET amb URL | username, name, email, id | 

Respostes:

1.- Code 200 Ok: 
    { "status": "success",
    "message": "Usuario encontrado",
    "data": {
    "id": 123,
    "username": "mara_gm",
    "email": "maragm@gmail.com",
    "name": "Mara"}

2.-  Code 404: 
    { "status": "error",
    "message": "Usuario no encontrado" }

3.- Code 400: 
    { "status": "error",
    "message": "Falta el parámetro 'username'"}

