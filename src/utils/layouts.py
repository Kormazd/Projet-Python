from dash import dcc, html
from src.components.bar_graph import BARG_HEIGHT, BARG_WIDTH, temperature_df as bargraph_df
from src.components.map import MAP_HEIGHT, MAP_WIDTH, temperature_df as map_df
from src.components.histogram import HISTOGRAM_HEIGHT, HISTOGRAM_WIDTH, temperature_df as histogram_df

PADDING = 30
BORDER_RADIUS = 10
BOX_SHADOW = "0 6px 12px rgba(0, 0, 0, 0.1)"

def centralized_layout():
    return html.Div([
        html.Div([
            html.H1("Dashboard Météo", 
                    style={'textAlign': 'center', 'color': '#007bff'}),
        ], style={'gridColumn': '1 / span 2'}),
        
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
        
        html.Div([
            html.Div([
                html.H2("Graphique des Températures Moyennes", style={'color': '#444'}),
                dcc.Graph(id='temperature-bargraph', style={
                    'height': BARG_HEIGHT+10,
                    'border': '1px solid #ddd',
                    'borderRadius': BORDER_RADIUS
                }),
            ], style={
                'width': '48%',
                'display': 'inline-block',
                'padding': '10px',
                'backgroundColor': 'white',
                'borderRadius': BORDER_RADIUS,
                'boxShadow': BOX_SHADOW
            }),
            
            html.Div([
                html.H2("Histogramme des Températures", style={'color': '#444'}),
                dcc.Graph(id='temperature-histogram', style={
                    'height': HISTOGRAM_HEIGHT+10,
                    'border': '1px solid #ddd',
                    'borderRadius': BORDER_RADIUS
                }),
            ], style={
                'width': '48%',
                'display': 'inline-block',
                'padding': '10px',
                'backgroundColor': 'white',
                'borderRadius': BORDER_RADIUS,
                'boxShadow': BOX_SHADOW
            })
        ], style={
            'gridColumn': '1 / span 2',
            'padding': PADDING
        }),
        
        html.Div([
            html.H2("Carte des Températures", style={'color': '#444'}),
            dcc.DatePickerSingle(
                id='date-picker',
                min_date_allowed=map_df['Date'].min().date(),
                max_date_allowed=map_df['Date'].max().date(),
                initial_visible_month=map_df['Date'].min().date(),
                date=map_df['Date'].min().date(),
            ),
            dcc.Graph(id='temperature-map', style={
                'height': MAP_HEIGHT,
                'border': '1px solid #ddd',
                'borderRadius': BORDER_RADIUS
            }),
        ], style={
            'gridColumn': '1 / span 2',
            'padding': PADDING,
            'backgroundColor': 'white',
            'borderRadius': BORDER_RADIUS,
            'boxShadow': BOX_SHADOW,
            'width': MAP_WIDTH + PADDING * 2
        })
        
    ], style={
        'display': 'grid',
        'gridTemplateColumns': '1fr',
        'gap': PADDING,
        'padding': PADDING,
        'backgroundColor': '#f0f0f0'
    })
