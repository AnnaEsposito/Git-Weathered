# consulta_api.py
import requests

def obtener_clima(ciudad):
    api_key = "d9cb110d0d56f149b5dec7fc0c1f1c37"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    parametros = {
        "q": ciudad,  # Nombre de la ciudad
        "appid": api_key,  # Tu clave de API
        "units": "metric"  # Opcional: para obtener la temperatura en grados Celsius
    }
    
    # Enviar la solicitud HTTP
    response = requests.get(base_url, params=parametros)
    
    if response.status_code == 200:
        data = response.json()
        # Procesar y retornar los datos relevantes
        temperatura = data['main']['temp']
        estado_clima = data['weather'][0]['description']
        return temperatura, estado_clima
    else:
        raise Exception(f"Error al consultar la API: {response.status_code}")

