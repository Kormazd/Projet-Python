from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from src.histogram import update_histogram, temperature_df as histogram_df
from src.map import update_map, temperature_df as map_df, geojson_data

# Layout principal
def create_layout():
    return html.Div([
        dcc.Tabs(
            id="navigation-tabs",
            value="histogram",
            children=[
                dcc.Tab(label="Histogramme", value="histogram", style={'padding': '10px', 'fontWeight': 'bold'}),
                dcc.Tab(label="Carte", value="map", style={'padding': '10px', 'fontWeight': 'bold'}),
            ],
            style={
                'backgroundColor': '#f9f9f9',
                'fontSize': '18px',
                'fontWeight': 'bold',
                'color': '#007bff'
            }
        ),
        html.Div(id="page-content", style={'padding': '20px'})
    ])

# Layout histogramme
def histogram_layout():
    return html.Div([
        html.H1("Évolution des Températures par Département", style={'textAlign': 'center'}),
        dcc.Dropdown(
            id='departement-dropdown',
            options=[{'label': dept, 'value': dept} for dept in sorted(histogram_df['Département'].unique())],
            value=sorted(histogram_df['Département'].unique())[0],
            placeholder="Sélectionnez un département",
        ),
        dcc.Graph(id='temperature-histogram'),
    ])

# Layout  carte
def map_layout():
    return html.Div([
        html.H1("Carte des Températures en France", style={'textAlign': 'center'}),
        dcc.DatePickerSingle(
            id='date-picker',
            min_date_allowed=map_df['Date'].min().date(),
            max_date_allowed=map_df['Date'].max().date(),
            initial_visible_month=map_df['Date'].min().date(),
            date=map_df['Date'].min().date(),
        ),
        dcc.Graph(id='temperature-map'),
    ])

# Configuration des callbacks
def register_callbacks(app):
    # Callback pour cahnger d'onglets
    @app.callback(
        Output('page-content', 'children'),
        [Input('navigation-tabs', 'value')]
    )
    def display_page(tab_value):
        if tab_value == "histogram":
            return histogram_layout()
        elif tab_value == "map":
            return map_layout()

    # Callback histogramme
    @app.callback(
        Output('temperature-histogram', 'figure'),
        [Input('departement-dropdown', 'value')]
    )
    def update_histogram_wrapper(selected_departement):
        return update_histogram(selected_departement)

    # Callback carte
    @app.callback(
        Output('temperature-map', 'figure'),
        [Input('date-picker', 'date')]
    )
    def update_map_wrapper(selected_date):
        return update_map(selected_date)
