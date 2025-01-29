# Definició dels EndPoints del Servei Web:

| Descripció | Host | End-point | Method | Tipus de petició | Paràmetres | 
|--------------|--------------|--------------|--------------|--------------|--------------|
| Servei que consulta un User per Username | 192.168.144.131:10050 | http://192.168.144.131:10050/tapatapp/getuser | GET | HTTP GET amb URL | username, name, email, id | 

Respostes:

1.- Code 200 Ok: 
    { "status": "success",
    "message": "Usuari trobat",
    "data": {
    "id": 123,
    "username": "mara_gm",
    "email": "maragm@gmail.com",
    "name": "Mara"}

2.-  Code 404: 
    { "status": "error",
    "message": "Usuari no trobat" }

3.- Code 400: 
    { "status": "error",
    "message": "Falta el paràmetre 'username'"}

