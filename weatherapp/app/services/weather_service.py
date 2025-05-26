import requests
import os
import json
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

BASE_DIR = Path(__file__).parent.parent.parent  # Ajuste para chegar na raiz do projeto

# --- Funções para carregar dados locais ---

def carregar_estados():
    path = BASE_DIR / "data" / "estados.json"
    with open(path, "r", encoding="utf-8-sig") as f:
        return json.load(f)

def carregar_municipios():
    path = BASE_DIR / "data" / "municipios.json"
    with open(path, "r", encoding="utf-8-sig") as f:
        return json.load(f)

def get_estados():
    """Retorna a lista de estados com dados do arquivo estados.json"""
    return carregar_estados()

def get_municipios_por_codigo_uf(codigo_uf):
    """Filtra e retorna municípios do estado pelo código_uf"""
    municipios = carregar_municipios()
    return [m for m in municipios if m.get("codigo_uf") == codigo_uf]

# --- Funções para consumir API WeatherAPI.com ---

def get_weather_for_city(lat, lon):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lon}&lang=pt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro ao buscar clima atual: {e}")
        return {"error": "Erro ao consultar API"}

def get_forecast_for_city(lat, lon, days=5):
    url = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={lat},{lon}&days={days}&lang=pt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("forecast", {}).get("forecastday", [])
    except Exception as e:
        print(f"Erro ao buscar previsão: {e}")
        return None
