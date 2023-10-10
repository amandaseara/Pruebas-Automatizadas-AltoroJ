import requests
from bs4 import BeautifulSoup

# Define la URL de AltoroJ
url = "http://localhost:8130/altoroj//search.jsp"

# Payload para XSS
payload = "<script>alert('Exitoso') ;</script>"

#Solicitud GET
query_param = "?query=" + payload
response = requests.get(url + query_param)

#Respuesta HTML
soup = BeautifulSoup(response.text, 'html.parser')

#Respuesta GET
if payload in str(soup):
    #Vulnerabilidad presente
    exit_code = 1
else:
    exit_code = 0

exit(exit_code)
