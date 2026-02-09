from flask import Blueprint, render_template, request, jsonify
from app.services.weather_service import get_estados, get_municipios_por_codigo_uf, get_weather_for_city, get_forecast_for_city

main_routes = Blueprint("main", __name__)

def get_estado_nome_por_codigo(codigo_uf):
    """Helper function to get estado nome by codigo_uf"""
    estados = get_estados()
    estado = next((e for e in estados if e["codigo_uf"] == codigo_uf), None)
    return estado["nome"] if estado else ""

@main_routes.route("/", methods=["GET", "POST"])
def home():
    estados = get_estados()

    if request.method == "POST":
        codigo_uf = int(request.form.get("estado"))
        municipio_nome = request.form.get("municipio")
        if not codigo_uf or not municipio_nome:
            return "Estado ou município não informado", 400

        municipios = get_municipios_por_codigo_uf(codigo_uf)
        municipio_data = next((m for m in municipios if m["nome"].lower() == municipio_nome.lower()), None)

        if not municipio_data:
            return "Município inválido ou não encontrado", 400

        lat = municipio_data.get("latitude")
        lon = municipio_data.get("longitude")
        if lat is None or lon is None:
            return "Coordenadas do município não encontradas", 400

        weather = get_weather_for_city(lat, lon)
        forecast = get_forecast_for_city(lat, lon)
        
        estado_nome = get_estado_nome_por_codigo(codigo_uf)

        estados = get_estados()
        return render_template(
            "index.html",
            estados=estados,
            municipios=municipios,
            estado_selecionado=codigo_uf,
            estado_selecionado_nome=estado_nome,
            municipio_selecionado=municipio_nome,
            weather=weather,
            forecast=forecast
        )

    # GET apenas mostra estados
    estados = get_estados()
    return render_template("index.html", estados=estados)


@main_routes.route("/municipios/<int:codigo_uf>")
def municipios_por_estado(codigo_uf):
    municipios = get_municipios_por_codigo_uf(codigo_uf)
    # Retornar só os nomes para o frontend popular o select
    lista_municipios = [m["nome"] for m in municipios]
    return jsonify(lista_municipios)
