# Definició dels EndPoints del Servei Web:

| Descripció | End-point | Method | Parametres | Resposta|
|--------------|--------------|--------------|--------------|--------------|
| Servei que consulta un User per Username | /users/getUser | GET | username | Code 200 Ok: {id=1,"username":"mara", "password":"garcia", "email":"maragm@gmail.com"}, Code 400 No trobat: {"error": "No trobat"} |


