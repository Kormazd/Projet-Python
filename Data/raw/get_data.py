import requests

# URL directe du fichier CSV
csv_url = "https://www.data.gouv.fr/fr/datasets/r/dd0df06a-85f2-4621-8b8b-5a3fe195bcd7"

# Nom du fichier local
output_file = "temperature_quotidienne.csv"

try:
    print("Téléchargement du fichier...")
    response = requests.get(csv_url)
    response.raise_for_status()  # Vérifie les erreurs HTTP
    print("Téléchargement réussi.")
    
    # Sauvegarder le fichier
    with open(output_file, "wb") as file:
        file.write(response.content)
    print(f"Fichier téléchargé et sauvegardé sous le nom '{output_file}'")
except requests.exceptions.RequestException as e:
    print(f"Erreur lors du téléchargement : {e}")
