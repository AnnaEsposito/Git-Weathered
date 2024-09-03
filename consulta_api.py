import requests
import json
import csv

# 2. Definir la URL y parámetros
api_key = "d9cb110d0d56f149b5dec7fc0c1f1c37"
base_url = "https://api.openweathermap.org/data/2.5/weather"

parametros = {
   
    "q": "Madrid",  # Nombre de la ciudad
    "appid": 'd9cb110d0d56f149b5dec7fc0c1f1c37'
,  # Tu clave de API
    "units": "metric"  # Opcional: para obtener la temperatura en grados Celsius
}

# 3. Enviar la solicitud HTTP
response = requests.get(base_url, params=parametros)

# 4. Manejar la respuestas
if response.status_code == 200:
    data = response.json()  # Parsear la respuesta JSON
    # 5. Procesar y mostrar los datos
    print(f"El clima en {data['name']} es {data['weather'][0]['description']}.")
    print(f"La temperatura actual es {data['main']['temp']} C.")
else:
    print("Hubo un problema al consultar la API. Código de estado:", response.status_code)
