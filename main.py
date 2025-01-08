import dash
from src.utils.layouts import centralized_layout
from src.utils.callbacks import register_callbacks

# Initialisation de l'application Dash
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Dashboard Météo"

# Définition du layout
app.layout = centralized_layout()

# Enregistrement des callbacks
register_callbacks(app)

# Lancement de l'application
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)

