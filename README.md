# Mi Aplicación CLI del Clima

Esta aplicación CLI permite conocer el estado climático de una ciudad específica usando la API de OpenWeatherMap. Puedes obtener la temperatura y el estado del clima en diferentes formatos: JSON, CSV o texto plano.

## Requisitos

- Python 3.x
- Las dependencias necesarias están listadas en `requirements.txt`.

## Instalación

1. Clona el repositorio o descarga los archivos del proyecto.

2. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

La aplicación CLI se ejecuta desde la línea de comandos con los siguientes parámetros:

- `--ciudad`: Nombre de la ciudad para la cual deseas obtener el clima.
- `--formato`: Formato de salida. Puede ser `json`, `csv`, o `texto`. El valor predeterminado es `texto`.

### Ejemplos de Uso

1. Obtener el clima en formato JSON:

    ```bash
    python app_clima.py --ciudad Madrid --formato json
    ```

2. Obtener el clima en formato CSV:

    ```bash
    python app_clima.py --ciudad Madrid --formato csv
    ```

3. Obtener el clima en formato texto:

    ```bash
    python app_clima.py --ciudad Madrid
    ```

4. Ver la ayuda disponible:

    ```bash
    python app_clima.py --help
    ```

## Scripts Adicionales

- `configurar_y_ejecutar.sh`: Script para ejecutar la aplicación con el parámetro de ayuda y para instalar las dependencias necesarias. Ejecuta el siguiente comando para correr el script:

    ```bash
    bash configurar_y_ejecutar.sh
    ```

## Pruebas

Las pruebas básicas están en `test_app_clima.py`. Actualmente, incluye una prueba dummy. Puedes agregar más pruebas utilizando `pytest`.

Para ejecutar las pruebas:

```bash
pytest
