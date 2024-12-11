from dash import Dash
from src.utils.layouts import create_layout
from src.utils.callbacks import register_callbacks

# Serveur dash
app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Températures en France"

# Initialisation layouts
app.layout = create_layout()

# Enregistrer callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
