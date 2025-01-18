import dash
import dash_bootstrap_components as dbc
from dash import html
from src.utils.layouts import centralized_layout
from src.utils.callbacks import register_callbacks

def create_app():
    """
    Crée et configure l'application Dash.
    Retourne une instance configurée avec layout et callbacks.
    """
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
    app.title = "Dashboard Météo"
    app.layout = html.Div(
        [centralized_layout()],
        style={'backgroundColor': '#fff', 'fontFamily': 'Arial, sans-serif'}
    )
    register_callbacks(app)  # Enregistre les callbacks pour interactivité
    return app

if __name__ == "__main__":
    # Lancement du serveur en mode debug
    app = create_app()
    app.run_server(debug=True, port=8050)
