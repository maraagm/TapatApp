# Definició dels EndPoints del Servei Web:

| Descripció | End-point | Method | Parametres | Resposta|
|--------------|--------------|--------------|--------------|--------------|
| Servei que consulta un User per Username | /users/getUser | GET | username | Code 200 Ok: {id=1,"username":"mara", "password":"garcia", "email":"maragm@gmail.com"}, Code 400 No trobat: {"error": "No trobat"} |

- Descripció: Servei que consulta un User per Username
- End-point: 192.168.144.131:10050/users/getUser
- Host: 192.168.144.131:10050
- Method: GET
- Parametres: username
- Resposta:

Code 200 Ok: {id=1,"username":"mara", "password":"garcia", "email":"maragm@gmail.com"}

Code 400 No trobat: {"error": "No trobat"}