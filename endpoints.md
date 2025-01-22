# Definició dels EndPoints del Servei Web:

- Descripció: Servei que consulta un User per Username
- End-point: 192.168.144.131:10050/users/getUser
- Host: 192.168.144.131:10050
- Method: GET
- Parametres: username
- Resposta:

Code 200 Ok: {id=1,"username":"mara", "password":"garcia", "email":"maragm@gmail.com"}

Code 400 No trobat: {"error": "No trobat"}