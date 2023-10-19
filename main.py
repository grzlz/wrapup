# 1. Crea un sistema que lleve datos de un API a una base de datos usando python (venv) y SQL.
# 2. Documenta todo el proceso utilizando Git y Github.
# 3. Credenciales de acceso a una base de datos en Postgres:
#    -Usuario: icarus-dev;
#    -Constraseña: pass-no-hackeable.


# Make request
import requests
import psycopg2

# Get names list
response = requests.get("https://pokeapi.co/api/v2/pokemon")
data = response.json() # dict
results = data["results"] # list
names = [result["name"] for result in results]

# Load data to database

db_params = {
    "host": "localhost",
    "database": "wrapup",
    "user": "icarus-dev",
    "password": "pass-no-hackeable"
}

connection = psycopg2.connect(**db_params)
cursor = connection.cursor()


print(names)

