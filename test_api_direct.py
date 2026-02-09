import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv('weatherapp/.env')

API_KEY = os.getenv("WEATHER_API_KEY")
print(f"API Key carregada: {API_KEY}")

# Testar API com Brasília
lat, lon = -15.7939, -47.8828

# Testar current weather
url_current = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lon}&lang=pt"
print(f"\nTestando URL: {url_current}")

try:
    response = requests.get(url_current)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:500]}")  # Primeiros 500 caracteres

    if response.status_code == 200:
        print("\n[OK] API funcionando corretamente!")
        data = response.json()
        print(f"Temperatura: {data['current']['temp_c']}°C")
        print(f"Condicao: {data['current']['condition']['text']}")
    else:
        print(f"\n[ERRO] Erro na API: {response.status_code}")
        print(f"Mensagem: {response.text}")

except Exception as e:
    print(f"\n[ERRO] Excecao: {e}")

# Testar forecast
print("\n" + "="*50)
url_forecast = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={lat},{lon}&days=5&lang=pt"
print(f"\nTestando URL de previsão: {url_forecast}")

try:
    response = requests.get(url_forecast)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:500]}")

    if response.status_code == 200:
        print("\n[OK] API de previsao funcionando!")
    else:
        print(f"\n[ERRO] Erro na API de previsao: {response.status_code}")

except Exception as e:
    print(f"\n[ERRO] Excecao: {e}")
