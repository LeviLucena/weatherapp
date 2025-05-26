<p align="center">
  <!-- Linguagem principal -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python Badge" />
  </a>

  <!-- Framework web -->
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask Badge" />
  </a>

  <!-- Engine de templates -->
  <a href="https://jinja.palletsprojects.com/">
    <img src="https://img.shields.io/badge/-Jinja2-B41717?style=flat-square&logo=jinja&logoColor=white" alt="Jinja2 Badge" />
  </a>

  <!-- Biblioteca para chamadas HTTP -->
  <a href="https://docs.python-requests.org/">
    <img src="https://img.shields.io/badge/-Requests-0078D7?style=flat-square&logo=python&logoColor=white" alt="Requests Badge" />
  </a>

  <!-- API de clima -->
  <a href="https://www.weatherapi.com/">
    <img src="https://img.shields.io/badge/-WeatherAPI-00A4DC?style=flat-square&logo=cloud&logoColor=white" alt="WeatherAPI Badge" />
  </a>

  <!-- Variáveis de ambiente -->
  <a href="https://pypi.org/project/python-dotenv/">
    <img src="https://img.shields.io/badge/-Dotenv-4E9A06?style=flat-square&logo=python&logoColor=white" alt="Dotenv Badge" />
  </a>

  <!-- Estrutura e dados locais -->
  <img src="https://img.shields.io/badge/-JSON%20Data-blue?style=flat-square&logo=json&logoColor=white" alt="JSON Data Badge" />

  <!-- Licença (editável conforme a sua) -->
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="License Badge" />

  <!-- Status -->
  <img src="https://img.shields.io/badge/status-estável-brightgreen?style=flat-square" alt="Status Badge" />
</p>

![Gemini_Generated_Image_wgu7wawgu7wawgu7](https://github.com/user-attachments/assets/147591d9-4874-40d9-a945-8bfd44cc8e2c)

# 🌦️ WeatherApp - Sistema de Previsões Climáticas

## ✅ Visão Geral

WeatherApp é um sistema web desenvolvido em Flask para exibir dados meteorológicos atuais e previsões para municípios brasileiros. O projeto utiliza a [WeatherAPI.com](https://www.weatherapi.com/) para consultar informações do clima, exibindo dados em português de forma clara e acessível para os usuários.

O diferencial deste projeto está na utilização de bases de dados locais (`estados.json` e `municipios.json`) contendo informações completas e coordenadas geográficas dos estados e municípios do Brasil, garantindo a seleção precisa e eficiente das localidades para consulta.

---

## 📌 Importância do Projeto

Com as mudanças climáticas e a crescente necessidade de planejamento baseado em condições meteorológicas, sistemas como o WeatherApp ajudam cidadãos, profissionais e gestores a tomarem decisões mais informadas, seja para o cotidiano, agricultura, transporte ou eventos.

Além disso, o projeto serve como base para aprendizado prático sobre:

- 🌐 Consumo de APIs externas de forma segura (com chave em `.env`)
- 🗺️ Estruturação e organização de dados geográficos locais
- 💻 Desenvolvimento web com Flask e templates Jinja2
- 📄 Tratamento e exibição de dados JSON em front-end
- 🚀 Boas práticas de organização de código e arquivos

## 🧪 Exemplo de Uso

https://github.com/user-attachments/assets/ac91025b-daf2-44bf-b321-98b088326127

---

## 🗂️ Estrutura do Projeto
```bash  
weatherapp/  
│  
├── app/  
│ ├── api/ # Roteadores das APIs (separados para funcionalidades REST)  
│ ├── services/ # Serviços para chamadas externas, como a WeatherAPI  
│ │ └── weather_service.py # Funções para buscar clima e previsões  
│ ├── templates/ # Arquivos HTML com Jinja2 para renderização dinâmica  
│ │ └── index.html # Página principal do app  
│ ├── static/ # Arquivos estáticos: CSS, JS, imagens, ícones  
│ └── routes.py # Rotas principais do Flask (lógica das views)  
│  
├── data/  
│ ├── estados.json # Dados dos estados brasileiros com coordenadas, códigos IBGE, etc.  
│ └── municipios.json # Dados dos municípios com coordenadas geográficas detalhadas  
│  
├── tests/  
│ └── test_api.py # Testes unitários das funcionalidades da API  
│  
├── run.py # Script para executar a aplicação Flask  
├── requirements.txt # Dependências Python do projeto  
└── .env # Arquivo com variáveis de ambiente (ex: WEATHER_API_KEY)  
```

---

## 📊 Detalhes dos Dados Geográficos

### estados.json

Contém informações dos 26 estados e do Distrito Federal do Brasil, incluindo:

- Código da UF (Unidade Federativa)
- Sigla da UF
- Nome completo do estado
- Coordenadas (latitude e longitude)
- Região do Brasil (Norte, Nordeste, Centro-Oeste, Sudeste, Sul)

Exemplo de entrada:

```json
{
  "codigo_uf": 35,
  "uf": "SP",
  "nome": "São Paulo",
  "latitude": -23.5489,
  "longitude": -46.6388,
  "regiao": "Sudeste"
}
```
### municipios.json
Contém dados detalhados de municípios brasileiros, incluindo:

- Código IBGE do município
- Nome do município
- Coordenadas geográficas (latitude, longitude)
- Código da UF
- Outras informações úteis como DDD, fuso horário, etc.

Exemplo de entrada:

```json
{
  "codigo_ibge": 3550308,
  "nome": "São Paulo",
  "latitude": -23.5505,
  "longitude": -46.6333,
  "capital": 1,
  "codigo_uf": 35,
  "siafi_id": 7107,
  "ddd": 11,
  "fuso_horario": "America/Sao_Paulo"
}
```
Esses arquivos permitem que o sistema ofereça seleção dinâmica de estado e município, além de garantir que as coordenadas corretas sejam usadas para consultar a API de clima.

## 🚀 Como Usar
### 1. Configuração

- Clone o repositório
```bash
git clone https://github.com/LeviLucena/weatherapp.git
cd weatherapp
```
- Crie um ambiente virtual Python
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
- Instale as dependências:
```bash
pip install -r requirements.txt
```
No arquivo .env na raiz do projeto, adicione sua chave da WeatherAPI:
```bash
WEATHER_API_KEY=Sua_Chave_Aqui
```
### 2. Executar a Aplicação
```bash
python run.py
```
### 3. Acessar no Navegador
Abra http://localhost:5000/ e selecione um estado e município para ver o clima atual e a previsão.

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- Flask (framework web)
- Requests (consumo da API externa)
- Jinja2 (template engine)
- JSON (dados geográficos)
- dotenv (variáveis de ambiente)

## 🌱 Próximos Passos e Melhorias
- Implementar cache para diminuir chamadas à API externa
- Adicionar suporte a gráficos com previsão em mais dias
- Permitir salvar municípios favoritos do usuário
- Internacionalizar o app para outros idiomas

## 📄 Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT) - veja o arquivo para detalhes.

## 🙋‍♂️ Contribuição
Contribuições são bem-vindas! Sinta-se livre para abrir issues ou pull requests.
