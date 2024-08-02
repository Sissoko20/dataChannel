import requests

url = "http://my-json-server.typicode.com/Sissoko20/dataChannel/channels"

try:
    response = requests.get(url)
    response.raise_for_status()  # Vérifie que la requête s'est bien passée
    data = response.json()
    print("Données récupérées avec succès:")
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la récupération des données: {e}")
