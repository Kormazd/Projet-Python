from dash import dcc, html
from src.components.barres_graphe import temperature_df as histogram_df
from src.components.map import temperature_df as map_df

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
                options=[{'label': dept, 'value': dept} for dept in sorted(histogram_df['Département'].unique())],
                value=sorted(histogram_df['Département'].unique())[0],
                placeholder="Sélectionnez un département",
            ),
            dcc.Graph(id='temperature-histogram', style={
                'height': '700px', 
                'border': '1px solid #ddd', 
                'borderRadius': '10px'
            }),
        ], style={
            'gridColumn': '1 / span 2', 
            'padding': '30px', 
            'backgroundColor': 'white', 
            'borderRadius': '10px', 
            'boxShadow': '0 6px 12px rgba(0, 0, 0, 0.1)'
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
                'height': '600px', 
                'border': '1px solid #ddd', 
                'borderRadius': '10px'
            }),
        ], style={
            'gridColumn': '1 / span 2', 
            'padding': '30px', 
            'backgroundColor': 'white', 
            'borderRadius': '10px', 
            'boxShadow': '0 6px 12px rgba(0, 0, 0, 0.1)'
        }),
        
    ], style={
        'display': 'grid',
        'gridTemplateColumns': '1fr',
        'gap': '30px',
        'padding': '30px',
        'backgroundColor': '#f0f0f0'
    })
