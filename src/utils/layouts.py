from dash import dcc, html
from src.components.bar_graph import BARG_HEIGHT, BARG_WIDTH, temperature_df as bargraph_df
from src.components.map import MAP_HEIGHT, MAP_WIDTH, temperature_df as map_df
from src.components.histogram import HISTOGRAM_HEIGHT, HISTOGRAM_WIDTH, temperature_df as histogram_df
from src.components.camembert import PIECHART_HEIGHT, temperature_df as piechart_df

PADDING = '20px'
BORDER_RADIUS = '12px'
BOX_SHADOW = '7px 7px 14px #c5c5c5, -7px -7px 14px #ffffff'



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
        # Titre principal
        html.Div([
            html.H1("Dashboard Météo", 
                    style={'textAlign': 'center', 'color': '#007bff'}),
        ], style={'gridColumn': '1 / span 2'}),
        
        # Dropdown pour les départements
        html.Div([
            html.H2("Évolution des Températures", style={'color': '#444'}),
            dcc.Dropdown(
                id='departement-dropdown',
                options=[{'label': dept, 'value': dept} for dept in sorted(bargraph_df['Département'].unique())],
                value=sorted(bargraph_df['Département'].unique())[0],
                placeholder="Sélectionnez un département",
            ),
        ], style={
            'gridColumn': '1 / span 2',
            'padding': PADDING
        }),
        
        # Section avec le bar graph et l'histogramme
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
            
            html.Div([
                html.H2("Histogramme des Températures", style={'color': '#444'}),
                dcc.Graph(id='temperature-histogram', style={
                    'height': HISTOGRAM_HEIGHT+10,
                    'border': '1px solid #ddd',
                    'borderRadius': BORDER_RADIUS
                }),
            ], style={
                'width': '47%',
                'display': 'inline-block',
                'marginLeft': '2%',
                'backgroundColor': 'white',
                'padding': '10px',
                'borderRadius': BORDER_RADIUS,
                'boxShadow': BOX_SHADOW
            })
        ], style={
            'gridColumn': '1 / span 2',
            'padding': PADDING
        }),
        
        # Section avec la carte
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
            'gridColumn': '1 / span 2',
            'padding': PADDING,
            'backgroundColor': 'white',
            'borderRadius': BORDER_RADIUS,
            'boxShadow': BOX_SHADOW,
            'width': MAP_WIDTH + PADDING * 2
        }),

        # Section avec le diagramme en camembert
        html.Div([
            html.Div([
                html.H2("Diagramme en Camembert des Températures", style={'color': '#444'}),
                dcc.DatePickerSingle(
                    id='pie-date-picker',
                    min_date_allowed=piechart_df['Date'].min().date(),
                    max_date_allowed=piechart_df['Date'].max().date(),
                    initial_visible_month=piechart_df['Date'].min().date(),
                    date=piechart_df['Date'].min().date(),
                ),
                dcc.Graph(id='temperature-piechart', style={
                    'height': PIECHART_HEIGHT,
                    'border': '1px solid #ddd',
                    'borderRadius': BORDER_RADIUS
                }),
            ], style={
                'backgroundColor': 'white',
                'padding': '10px',
                'borderRadius': BORDER_RADIUS,
                'boxShadow': BOX_SHADOW,
                'marginTop': '30px',
            })
        ], style={
            'gridColumn': '1 / span 2',
            'padding': PADDING
        }),
        
    ], style={
        'maxWidth': '1200px',
        'margin': '0 auto',
        'padding': '20px',
        'fontFamily': 'Arial, sans-serif'
    })
