import dash
import dash_bootstrap_components as dbc
from dash import html
from src.utils.layouts import centralized_layout
from src.utils.callbacks import register_callbacks

# Initialisation de l'application Dash avec un thème Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
app.title = "Dashboard Météo"

# Définition du layout avec du style global
app.layout = html.Div([
    centralized_layout(),
    html.Footer("Données météorologiques fournies par Météo France", 
                style={
                    'textAlign': 'center', 
                    'padding': '10px', 
                    'backgroundColor': '#1a1a1a', 
                    'color': 'white',
                    'marginTop': '20px'
                })
], style={
    'backgroundColor': '#f5f5f5',
    'fontFamily': 'Arial, sans-serif'
})

# Enregistrement des callbacks
register_callbacks(app)

# Lancement de l'application
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
