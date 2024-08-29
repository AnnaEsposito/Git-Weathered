
import argparse
parser = argparse.ArgumentParser(description="APP DEL CLIMA: Esta aplicación te permite conocer el estado climático de una ciudad en concreto.\n\n"
                "Para el efecto debes introducir los siguientes datos:\n"
                "--ciudad: Nombre de la ciudad.\n"
                "--formato: Formato de salida (json, csv, texto)." )
parser.add_argument('--ciudad', type=str, required=True,help='Debes proporcionar el parametro ciudad a traves de la terminal,\n'
                    'de la siguiente forma: python app_clima.py --ciudad #Ejemp:Madrid')
parser.add_argument('--formato', type=str, choices=['json','csv','texto'], default='texto',help='Debes indicar el formato de salida (json o csv o texto)\n'
                    'de la misma forma: python app_clima.py --formato #Ejemp:json')

args = parser.parse_args()

