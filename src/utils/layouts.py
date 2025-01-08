from dash import dcc, html
from src.components.histogram import temperature_df as histogram_df
from src.components.map import temperature_df as map_df
#from src.components.highscores import get_highscores

# Layout principal
def create_layout():
    return html.Div([
        dcc.Tabs(
            id="navigation-tabs",
            value="histogram",
            children=[
                dcc.Tab(label="Histogramme", value="histogram", style={'padding': '10px', 'fontWeight': 'bold'}),
                dcc.Tab(label="Carte", value="map", style={'padding': '10px', 'fontWeight': 'bold'}),
                dcc.Tab(label="Battle", value="battle", style={'padding': '10px', 'fontWeight': 'bold'})
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

# Layout carte
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

# Layout bataille des départements
def battle_layout():
    return html.Div([
        html.H1("Bataille des Départements", style={'textAlign': 'center'}),
        html.Div([
            dcc.Dropdown(
                id='dept1-dropdown',
                options=[{'label': dept, 'value': dept} for dept in sorted(histogram_df['Département'].unique())],
                value=sorted(histogram_df['Département'].unique())[0],
                placeholder="Sélectionnez le premier département",
            ),
            dcc.Dropdown(
                id='dept2-dropdown',
                options=[{'label': dept, 'value': dept} for dept in sorted(histogram_df['Département'].unique())],
                value=sorted(histogram_df['Département'].unique())[1],
                placeholder="Sélectionnez le second département",
            ),
            dcc.RadioItems(
                id='year-selector',
                options=[
                    {'label': '1 an', 'value': 1},
                    {'label': '2 ans', 'value': 2},
                    {'label': '3 ans', 'value': 3}
                ],
                value=1,
                labelStyle={'margin-right': '10px'}
            ),
        ], style={'display': 'flex', 'flexDirection': 'column', 'gap': '10px', 'marginBottom': '20px'}),
        html.Div(id='battle-results', style={'marginTop': '20px'}),
    ])
"""
def highscores_layout():
    return html.Div([
        html.H1("High Scores des Températures", style={'textAlign': 'center'}),
        html.Button("Mettre à jour", id="update-button", n_clicks=0),
        html.Div(id="highscores-table")
    ])
"""