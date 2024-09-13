
import argparse
import sys  # Importa el módulo sys
import json
import csv
from consulta_api import obtener_clima

#Definir los parametros de la aplicacion CLI con "argparse".
def main():
    parser = argparse.ArgumentParser(description="APP DEL CLIMA: Esta aplicación te permite conocer el estado climático de una ciudad en concreto.\n\n"
                "Para el efecto debes introducir los siguientes datos:\n"
                "--ciudad: Nombre de la ciudad.\n"
                "--formato: Formato de salida (json, csv, texto)." )

    parser.add_argument('--ciudad', type=str, required=True, help='Debes proporcionar el parametro ciudad a traves de la terminal,\n'
                        'de la siguiente forma: python app_clima.py --ciudad #Ejemp:Madrid')

    parser.add_argument('--formato', type=str, choices=['json', 'csv', 'texto'], default='texto', help='Debes indicar el formato de salida (json o csv o texto)\n'
                        'de la misma forma: python app_clima.py --formato #Ejemp:json')

    args = parser.parse_args()
    
    
    try:
        temperatura, estado_clima = obtener_clima(args.ciudad)
        resultado = {
            "temperatura": temperatura,
            "estado_clima": estado_clima
        }
        
        if args.formato == 'json':
            print(json.dumps(resultado, indent=4))
        elif args.formato == 'csv':
            writer = csv.writer(sys.stdout)
            writer.writerow(["temperatura", "estado_clima"])
            writer.writerow([temperatura, estado_clima])
        else:
            print(f"El clima en {args.ciudad} es {estado_clima}.")
            print(f"La temperatura actual es {temperatura} C.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
