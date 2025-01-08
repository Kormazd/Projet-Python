from dash import dcc, html
from src.components.histogram import temperature_df as histogram_df
from src.components.map import temperature_df as map_df

def centralized_layout():
    return html.Div([
        html.Div([
            html.H1("Dashboard Météo", style={'textAlign': 'center'}),
        ], style={'gridColumn': '1 / span 3'}),
        
        html.Div([
            html.H2("Carte des Températures"),
            dcc.DatePickerSingle(
                id='date-picker',
                min_date_allowed=map_df['Date'].min().date(),
                max_date_allowed=map_df['Date'].max().date(),
                initial_visible_month=map_df['Date'].min().date(),
                date=map_df['Date'].min().date(),
            ),
            dcc.Graph(id='temperature-map', style={'height': '400px'}),
        ], style={'gridColumn': '1 / 2'}),
        
        html.Div([
            html.H2("Évolution des Températures"),
            dcc.Dropdown(
                id='departement-dropdown',
                options=[{'label': dept, 'value': dept} for dept in sorted(histogram_df['Département'].unique())],
                value=sorted(histogram_df['Département'].unique())[0],
                placeholder="Sélectionnez un département",
            ),
            dcc.Graph(id='temperature-histogram', style={'height': '400px'}),
        ], style={'gridColumn': '2 / 3'}),
        
        html.Div([
            html.H2("Bataille des Départements"),
            html.Div([
                dcc.Dropdown(
                    id='dept1-dropdown',
                    options=[{'label': dept, 'value': dept} for dept in sorted(histogram_df['Département'].unique())],
                    value=sorted(histogram_df['Département'].unique())[0],
                    placeholder="Département 1",
                ),
                dcc.Dropdown(
                    id='dept2-dropdown',
                    options=[{'label': dept, 'value': dept} for dept in sorted(histogram_df['Département'].unique())],
                    value=sorted(histogram_df['Département'].unique())[1],
                    placeholder="Département 2",
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
            ], style={'display': 'flex', 'gap': '10px'}),
            html.Div(id='battle-results'),
        ], style={'gridColumn': '1 / span 3'}),
    ], style={
        'display': 'grid',
        'gridTemplateColumns': '1fr 1fr',
        'gap': '20px',
        'padding': '20px'
    })
