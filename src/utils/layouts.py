from dash import dcc, html
from src.components.bar_graph import temperature_df as bargraph_df
from src.components.map import temperature_df as map_df
from src.components.histogram import temperature_df as histogram_df

# Style unifié pour les titres
TITLE_STYLE = {
    'fontSize': '1.4em',
    'fontWeight': 'bold',
    'color': '#333',
    'marginBottom': '10px'
}

# Style néomorphique pour les “fenêtres” (en blanc)
NEOMORPHISM_BOX_STYLE = {
    'backgroundColor': '#ffffff',
    'borderRadius': '12px',
    'boxShadow': '7px 7px 14px #c5c5c5, -7px -7px 14px #ffffff',
    'padding': '20px',
    'marginBottom': '30px'
}

def centralized_layout():
    """
    Construit et renvoie l'agencement global du dashboard (layout).
    """
    return html.Div([
        html.H2(
            "Dashboard Météo",
            style={
                **TITLE_STYLE,
                'textAlign': 'center',
                'color': '#007bff',
                'marginBottom': '20px'
            }
        ),
        
        html.Div([
            html.Div([
                html.H2("Évolution des Températures", style=TITLE_STYLE),
                dcc.Dropdown(
                    id='departement-dropdown',
                    options=[
                        {'label': dept, 'value': dept}
                        for dept in sorted(bargraph_df['Département'].unique())
                    ],
                    value=sorted(bargraph_df['Département'].unique())[0],
                    placeholder="Sélectionnez un département",
                    style={'width': '300px', 'margin': '0 auto'}
                ),
            ], style={
                'textAlign': 'center',
                **NEOMORPHISM_BOX_STYLE
            }),
        ], style={'marginBottom': '30px'}),

        html.Div([
            html.Div([
                html.H2("Graphique des Températures Moyennes", style=TITLE_STYLE),
                dcc.Graph(id='temperature-bargraph'),
            ], style={
                'flex': '1',
                'marginRight': '10px',
                **NEOMORPHISM_BOX_STYLE
            }),

            html.Div([
                html.H2("Histogramme des Températures", style=TITLE_STYLE),
                dcc.Graph(id='temperature-histogram'),
            ], style={
                'flex': '1',
                'marginLeft': '10px',
                **NEOMORPHISM_BOX_STYLE
            }),
        ], style={
            'display': 'flex',
            'justifyContent': 'space-between',
            'marginBottom': '30px'
        }),

        html.Div([
            html.Div([
                html.H2("Carte des Températures", style=TITLE_STYLE),
                dcc.DatePickerSingle(
                    id='date-picker',
                    min_date_allowed=map_df['Date'].min().date(),
                    max_date_allowed=map_df['Date'].max().date(),
                    initial_visible_month=map_df['Date'].min().date(),
                    date=map_df['Date'].min().date(),
                    style={'marginBottom': '20px'}
                ),
                dcc.Graph(id='temperature-map'),
            ], style={
                'flex': '1',
                'marginRight': '10px',
                **NEOMORPHISM_BOX_STYLE
            }),

            html.Div([
                html.H2("Répartition des Températures (Camembert)", style=TITLE_STYLE),
                dcc.Graph(id='temperature-pie'),
            ], style={
                'flex': '1',
                'marginLeft': '10px',
                **NEOMORPHISM_BOX_STYLE
            }),
        ], style={
            'display': 'flex',
            'justifyContent': 'space-between'
        }),
    ], style={
        'maxWidth': '1200px',
        'margin': '0 auto',
        'padding': '20px',
        'fontFamily': 'Arial, sans-serif'
    })
