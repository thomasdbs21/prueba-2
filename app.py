import os
import requests

API_KEY = os.getenv("API_KEY_PROYECTO")
CIUDAD = "Santiago"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CIUDAD}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url, timeout=5)

    if response.status_code == 401:
        print("ERROR: API KEY inválida")
        exit()

    if response.status_code == 404:
        print("ERROR: Ciudad no encontrada")
        exit()

    response.raise_for_status()

    data = response.json()

    temperatura = data["main"]["temp"]
    humedad = data["main"]["humidity"]
    viento = data["wind"]["speed"]

    print("===== CLIMA ACTUAL =====")
    print(f"Temperatura: {temperatura}°C")
    print(f"Humedad: {humedad}%")
    print(f"Viento: {viento} m/s")

except requests.exceptions.Timeout:
    print("ERROR: Timeout")

except requests.exceptions.ConnectionError:
    print("ERROR: Conexión")

except requests.exceptions.RequestException as e:
    print(f"ERROR GENERAL: {e}")
