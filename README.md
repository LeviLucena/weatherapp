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

  <!-- Licença -->
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="License Badge" />

  <!-- Status -->
  <img src="https://img.shields.io/badge/status-estável-brightgreen?style=flat-square" alt="Status Badge" />
</p>

![Gemini_Generated_Image_wgu7wawgu7wawgu7](https://github.com/user-attachments/assets/147591d9-4874-40d9-a945-8bfd44cc8e2c)

# 🌦️ WeatherApp - Sistema de Previsões Climáticas

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Importância do Projeto](#-importância-do-projeto)
- [Funcionalidades](#-funcionalidades)
- [Exemplo de Uso](#-exemplo-de-uso)
- [Estrutura do Projeto](#️-estrutura-do-projeto)
- [Detalhes dos Dados Geográficos](#-detalhes-dos-dados-geográficos)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Como Executar](#-como-executar)
- [Executando Testes](#-executando-testes)
- [Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [Troubleshooting](#-troubleshooting)
- [Próximos Passos](#-próximos-passos-e-melhorias)
- [Licença](#-licença)
- [Contribuição](#️-contribuição)

---

## ✅ Visão Geral

**WeatherApp** é um sistema web desenvolvido em **Flask** para exibir dados meteorológicos atuais e previsões para municípios brasileiros. O projeto utiliza a [WeatherAPI.com](https://www.weatherapi.com/) para consultar informações do clima, exibindo dados em português de forma clara e acessível para os usuários.

O diferencial deste projeto está na utilização de **bases de dados locais** (`estados.json` e `municipios.json`) contendo informações completas e coordenadas geográficas dos estados e municípios do Brasil, garantindo a seleção precisa e eficiente das localidades para consulta.

---

## 📌 Importância do Projeto

Com as mudanças climáticas e a crescente necessidade de planejamento baseado em condições meteorológicas, sistemas como o WeatherApp ajudam cidadãos, profissionais e gestores a tomarem decisões mais informadas, seja para o cotidiano, agricultura, transporte ou eventos.

Além disso, o projeto serve como base para aprendizado prático sobre:

- 🌐 **Consumo de APIs externas** de forma segura (com chave em `.env`)
- 🗺️ **Estruturação e organização** de dados geográficos locais
- 💻 **Desenvolvimento web** com Flask e templates Jinja2
- 📄 **Tratamento e exibição** de dados JSON no front-end
- 🚀 **Boas práticas** de organização de código e arquivos
- ✅ **Testes unitários** e validação de APIs

---

## 🚀 Funcionalidades

Este sistema de previsão do tempo permite que o usuário:

### 📍 Clima Atual
- 🔍 Selecione o **estado (UF)** e **município** de interesse em listas dinâmicas (dependentes)
- 🌡️ Visualize dados meteorológicos atuais, incluindo:
  - Temperatura atual e sensação térmica
  - Umidade do ar
  - Velocidade e direção do vento
  - Pressão atmosférica
  - Visibilidade
  - Índice UV
  - Cobertura de nuvens
  - Condição do céu (ensolarado, nublado, chuvoso, etc.)

### 📅 Previsão Estendida
- Previsão para os **próximos 5 dias**, com:
  - Temperaturas máximas e mínimas
  - Ícones e descrições das condições do tempo
  - Chance de chuva
  - Informações por data

### 🌙 Dados Astronômicos
- Horários de nascer e pôr do sol
- Horários de nascer e pôr da lua
- Fase da lua
- Iluminação lunar

### 🗺️ Dados Geográficos
- Utiliza arquivos locais `estados.json` e `municipios.json` para:
  - Garantir maior velocidade na navegação
  - Evitar chamadas desnecessárias à API
  - Fornecer coordenadas precisas de todos os municípios brasileiros

### 💡 Interface
- Interface leve com HTML + CSS puro (via Jinja2)
- Design responsivo e intuitivo
- Integração via Flask com atualização dinâmica

---

## 🧪 Exemplo de Uso

https://github.com/user-attachments/assets/ac91025b-daf2-44bf-b321-98b088326127

---

## 🗂️ Estrutura do Projeto

```bash
weatherapp/
│
├── weatherapp/                    # Diretório principal da aplicação
│   │
│   ├── app/                       # Módulo principal da aplicação
│   │   ├── __init__.py           # Marcador de pacote Python
│   │   ├── routes.py             # Rotas principais do Flask
│   │   │
│   │   ├── services/             # Serviços para chamadas externas
│   │   │   ├── __init__.py       # Marcador de pacote Python
│   │   │   └── weather_service.py # Funções para buscar clima e previsões
│   │   │
│   │   └── templates/            # Arquivos HTML com Jinja2
│   │       └── index.html        # Página principal do app
│   │
│   ├── static/                    # Arquivos estáticos
│   │   ├── style.css             # Estilos CSS
│   │   ├── script.js             # Scripts JavaScript
│   │   └── logo.png              # Logo da aplicação
│   │
│   ├── data/                      # Dados geográficos locais
│   │   ├── estados.json          # Dados dos estados brasileiros
│   │   └── municipios.json       # Dados dos municípios brasileiros
│   │
│   ├── tests/                     # Testes unitários
│   │   ├── __init__.py           # Marcador de pacote Python
│   │   └── test_api.py           # Testes das funcionalidades da API
│   │
│   ├── run.py                     # Script para executar a aplicação Flask
│   ├── run_tests.py              # Script para executar os testes
│   └── .env                       # Variáveis de ambiente (API KEY)
│
├── test_api_direct.py            # Script de diagnóstico da API
├── requirements.txt              # Dependências Python do projeto
└── README.md                     # Documentação do projeto
```

---

## 📊 Detalhes dos Dados Geográficos

### 📍 estados.json

Contém informações dos **26 estados** e do **Distrito Federal** do Brasil, incluindo:

- Código da UF (Unidade Federativa)
- Sigla da UF
- Nome completo do estado
- Coordenadas (latitude e longitude)
- Região do Brasil (Norte, Nordeste, Centro-Oeste, Sudeste, Sul)

**Exemplo de entrada:**

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

### 🏙️ municipios.json

Contém dados detalhados de **todos os municípios brasileiros**, incluindo:

- Código IBGE do município
- Nome do município
- Coordenadas geográficas (latitude, longitude)
- Código da UF
- Capital (0 ou 1)
- SIAFI ID
- DDD
- Fuso horário

**Exemplo de entrada:**

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

---

## 🔧 Instalação e Configuração

### Pré-requisitos

- **Python 3.8+** instalado
- Conexão com a internet (para acessar a API)
- Chave de API da WeatherAPI (gratuita)

### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/LeviLucena/weatherapp.git
cd weatherapp
```

### 2️⃣ Crie um Ambiente Virtual (Recomendado)

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Anaconda/Miniconda:**
```bash
conda create -n weatherapp python=3.9
conda activate weatherapp
```

### 3️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

**Dependências principais:**
- Flask
- requests
- python-dotenv

### 4️⃣ Configure a Chave da API

1. Acesse [WeatherAPI.com](https://www.weatherapi.com/signup.aspx) e crie uma conta gratuita
2. Após criar a conta, vá para o **painel de controle** e copie sua **API Key**
3. Abra o arquivo `weatherapp/.env` e substitua pela sua chave:

```env
WEATHER_API_KEY=sua_chave_api_aqui
```

**⚠️ Importante:** Não compartilhe sua chave de API publicamente!

---

## ▶️ Como Executar

### Executar a Aplicação

1. Navegue até o diretório do projeto:
```bash
cd weatherapp/weatherapp
```

2. Execute a aplicação:
```bash
python run.py
```

3. Acesse no navegador:
```
http://localhost:5000
```

ou

```
http://127.0.0.1:5000
```

### Parar a Aplicação

Pressione `CTRL + C` no terminal onde a aplicação está rodando.

---

## 🧪 Executando Testes

### Testes Unitários Completos

Para executar todos os testes unitários:

```bash
cd weatherapp/weatherapp
python run_tests.py
```

**Saída esperada:**
```
test_get_weather_for_city (tests.test_api.TestWeatherAPI.test_get_weather_for_city) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.253s

OK
```

### Teste de Diagnóstico da API

Para verificar se a API está funcionando corretamente:

```bash
cd weatherapp
python test_api_direct.py
```

**Saída esperada:**
```
API Key carregada: sua_chave_aqui

Testando URL: https://api.weatherapi.com/v1/current.json...
Status Code: 200
[OK] API funcionando corretamente!
Temperatura: 25.1°C
Condicao: Parcialmente nublado

==================================================

Testando URL de previsao: https://api.weatherapi.com/v1/forecast.json...
Status Code: 200
[OK] API de previsao funcionando!
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição | Versão |
|------------|-----------|--------|
| **Python** | Linguagem de programação principal | 3.8+ |
| **Flask** | Framework web minimalista | 2.x |
| **Requests** | Biblioteca para requisições HTTP | 2.x |
| **Jinja2** | Engine de templates | 3.x |
| **python-dotenv** | Gerenciamento de variáveis de ambiente | 1.x |
| **WeatherAPI** | API de dados meteorológicos | v1 |
| **JSON** | Formato de dados geográficos | - |
| **HTML5/CSS3** | Interface do usuário | - |

---

## 🔍 Troubleshooting

### ❌ Erro: "ModuleNotFoundError: No module named 'app'"

**Causa:** Faltam os arquivos `__init__.py` nos diretórios.

**Solução:** Certifique-se de que os seguintes arquivos existem:
- `weatherapp/app/__init__.py`
- `weatherapp/app/services/__init__.py`
- `weatherapp/tests/__init__.py`

### ❌ Erro: "API Key inválida" ou "Status 401"

**Causa:** Chave da API incorreta ou não configurada.

**Solução:**
1. Verifique se o arquivo `.env` existe em `weatherapp/.env`
2. Confirme que a chave está correta (sem espaços extras)
3. Teste a chave com o script `test_api_direct.py`

### ❌ Erro: "No module named 'flask'"

**Causa:** Dependências não instaladas.

**Solução:**
```bash
pip install -r requirements.txt
```

### ❌ Erro: "Port 5000 already in use"

**Causa:** Outra aplicação está usando a porta 5000.

**Solução:**
1. Pare a outra aplicação, ou
2. Modifique a porta em `run.py`:
```python
app.run(debug=True, port=5001)
```

### ❌ Dados não aparecem na interface

**Causa:** Problema na API ou nas coordenadas.

**Solução:**
1. Execute `test_api_direct.py` para verificar a API
2. Verifique os logs no console onde o Flask está rodando
3. Confirme que os arquivos `estados.json` e `municipios.json` existem em `weatherapp/data/`

### ❌ Erro de encoding no Windows

**Causa:** Caracteres especiais em português.

**Solução:** Execute o terminal com encoding UTF-8:
```bash
chcp 65001
```

---

## 🌱 Próximos Passos e Melhorias

- [ ] Implementar **cache** para diminuir chamadas à API externa
- [ ] Adicionar suporte a **gráficos interativos** com previsão em mais dias
- [ ] Permitir salvar **municípios favoritos** do usuário (localStorage)
- [ ] Internacionalizar o app para **outros idiomas** (inglês, espanhol)
- [ ] Adicionar **modo escuro/claro**
- [ ] Implementar **API REST** para consumo externo
- [ ] Adicionar **mapas interativos** com visualização geográfica
- [ ] Implementar **notificações** de alertas meteorológicos
- [ ] Adicionar **comparação** entre múltiplas cidades
- [ ] Criar **dashboard** com histórico de consultas

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

```
MIT License

Copyright (c) 2026 Levi Lucena

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙋‍♂️ Contribuição

Contribuições são **muito bem-vindas**! Sinta-se à vontade para:

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. **Push** para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um **Pull Request**

### Como Contribuir

- 🐛 Reporte bugs abrindo uma [issue](https://github.com/LeviLucena/weatherapp/issues)
- 💡 Sugira novas funcionalidades
- 📝 Melhore a documentação
- ✨ Implemente novas features
- 🧪 Adicione mais testes

---

## 👤 Autor

**Levi Lucena**

- GitHub: [@LeviLucena](https://github.com/LeviLucena)
- LinkedIn: [Levi Lucena](https://www.linkedin.com/in/levilucena/)

---

## 🌟 Agradecimentos

- [WeatherAPI.com](https://www.weatherapi.com/) - API de dados meteorológicos
- [Flask](https://flask.palletsprojects.com/) - Framework web
- [IBGE](https://www.ibge.gov.br/) - Dados geográficos do Brasil

---

## 📞 Suporte

Se você tiver alguma dúvida ou problema, por favor:

1. Verifique a seção [Troubleshooting](#-troubleshooting)
2. Consulte as [Issues](https://github.com/LeviLucena/weatherapp/issues) existentes
3. Abra uma nova [Issue](https://github.com/LeviLucena/weatherapp/issues/new) se necessário

---

<p align="center">
  Feito com ❤️ por <a href="https://github.com/LeviLucena">Levi Lucena</a>
</p>

<p align="center">
  <sub>⭐ Se este projeto te ajudou, deixe uma estrela!</sub>
</p>
