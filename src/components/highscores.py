import pandas as pd
from dash import Input, Output, dash_table, html, dash

# Charger et transformer les données
def calculate_highscores(file_path):
    temperature_df = pd.read_csv(file_path, delimiter=';')
    temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])
    temperature_df['Year'] = temperature_df['Date'].dt.year
    temperature_df['Month'] = temperature_df['Date'].dt.month
    temperature_df['Season'] = temperature_df['Month'].apply(lambda x: (
        'Winter' if x in [12, 1, 2] else
        'Spring' if x in [3, 4, 5] else
        'Summer' if x in [6, 7, 8] else
        'Autumn'
    ))
    temperature_df = temperature_df.dropna(subset=['TMax (°C)'])
    highscores = (
        temperature_df.groupby(['Year', 'Season'])
        .agg(Max_Temperature=('TMax (°C)', 'max'))
        .reset_index()
    )
    return highscores

# Exposer la fonction pour Dash
def get_highscores_table(highscores):
    return html.Div([
        html.H1("High Scores des Températures", style={'textAlign': 'center'}),
        dash_table.DataTable(
            id='highscores-table',
            columns=[
                {'name': 'Année', 'id': 'Year'},
                {'name': 'Saison', 'id': 'Season'},
                {'name': 'Température Max (°C)', 'id': 'Max_Temperature'}
            ],
            data=highscores.to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            },
            style_cell={
                'textAlign': 'center',
                'padding': '10px'
            }
        )
    ])

def update_highscores_table(n_clicks, file_path):
    if n_clicks:
        highscores_df = calculate_highscores(file_path)
        return highscores_df.to_dict('records')
    return dash.no_update
