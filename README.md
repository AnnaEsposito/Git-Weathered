# Weather API CLI Python 🌦️
This project is a Command Line Interface (CLI) application in Python that retrieves the current weather of any city using the [OpenWeatherMap API](https://openweathermap.org/current). It's a great way to get familiar with API consumption, argument handling, and output formats like JSON, CSV, or plain text.

## 🚀 What does this app do?
It fetches the current weather information of any city in the world and displays the data in different formats.

## 📦 Project structure
```bash
clima-api-cli-python/
├── app_clima.py # Main script that takes terminal arguments
├── consulta_api.py # Handles the weather API request
├── README.md # Project documentation
```

## 🧰 Technologies used
- Python 3.x
- Requests library
- OpenWeatherMap API

## ⚙️ Installation
1. Clone the repository:
```bash
git clone https://github.com/AnnaEsposito/edu-clima-api-cli-python.git
cd edu-clima-api-cli-python
```
2. Get your own API key from OpenWeatherMap and add it inside consulta_api.py.

## 🧪 Running the app
From your terminal:
python app_clima.py --ciudad "Asuncion" --formato json
You can change the --formato argument to one of the supported formats: json, csv, or text.

