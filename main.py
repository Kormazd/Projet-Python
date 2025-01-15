import dash
import dash_bootstrap_components as dbc
from dash import html
from src.utils.layouts import centralized_layout
from src.utils.callbacks import register_callbacks

def create_app():
    """
    Crée et configure l'application Dash.
    """
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
    app.title = "Dashboard Météo"
    app.layout = html.Div([
        centralized_layout(),
    ], style={
        'backgroundColor': '#fff',  
        'fontFamily': 'Arial, sans-serif'
    })
    register_callbacks(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run_server(debug=True, port=8050)
