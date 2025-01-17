import requests

# URL du fichier CSV
csv_url = "https://files.data.gouv.fr/dd0df06a-85f2-4621-8b8b-5a3fe195bcd7/20230101-20231231.csv"

# Nom du fichier à sauvegarder localement
output_file = "/raw/temperature_quotidienne.csv"

try:
    # Récupérer les données depuis l'URL
    response = requests.get(csv_url)
    response.raise_for_status()  # Vérifie les erreurs HTTP
    
    # Sauvegarder le fichier localement
    with open(output_file, "wb") as file:
        file.write(response.content)
    
    print(f"Fichier téléchargé et sauvegardé sous le nom '{output_file}'")
except requests.exceptions.RequestException as e:
    print(f"Erreur lors du téléchargement : {e}")