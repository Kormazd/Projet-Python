User Guide :
Télécharger le dossier zippé sur votre machine à partir du lien github
Installer les dépendances :
pip install -r requirements.txt
Lancer le dashboard :
python main.py 
Cliqué sur le lien qui s'affiche alors dans le terminal. 
Comme ça vous tomberez sur notre dashboard qui contient un histogramme et une carte concernant les températures moyennes dans les départements de France.

Data :
Il y a un set de donnée qui contient toutes les données concernant les températures départementales par jour en France entre 2018 et octobre 2024.
Un fihcier Geojson est aussi utilisé pour nous permettre de faire la carte sur un fond déjà existant.

Developper Guide :
Architecture du projet : 
graph 
    main.py --> src
    src --> components
    src --> utils
    components --> histogram.py
    components --> map.py
    utils --> layouts.py
    utils --> callbacks.py
    utils --> config.py

Ajouter un nouvel onglet ou une nouvelle page :
Créer un fichier dans src/pages pour la nouvelle page.
Ajouter un layout spécifique pour cette page dans src/utils/layouts.py.
Ajouter un onglet dans le layout principal pour accéder à cette page.
Gérer les callbacks spécifiques à cette page dans src/utils/callbacks.py.

Ajouter un nouveau composant :
Créer un fichier Python dans src/components.
Définir le composant en utilisant les données nécessaires et les bibliothèques appropriées (ex. Plotly, Dash).
Intégrer ce composant dans une page existante ou nouvelle via son layout.

Rapport d'analyse :
Principales Conclusions
Les températures moyennes en France ont augmenté entre 2018 et 2024, avec des étés de plus en plus chauds.
Les départements du sud présentent des températures moyennes plus élevées que ceux du nord.
Une forte corrélation est observée entre les températures moyennes (TMoy (°C)) et maximales (TMax (°C)).
Recommandations
Continuer à collecter et analyser les données pour suivre les tendances climatiques.
Envisager des stratégies d’adaptation pour les régions les plus touchées.

Copyright :
Je déclare sur l’honneur que le code fourni a été produit par moi-même, sauf pour les éléments suivants :
Plotly Express et Dash : Syntaxes et concepts issus de la documentation officielle (Plotly, Dash).
Toute ligne non déclarée ci-dessus est réputée être originale.