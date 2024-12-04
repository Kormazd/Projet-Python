import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Charger le fichier CSV
file_path = 'Data/raw/temperature-quotidienne-departementale.csv' 
temperature_df = pd.read_csv(file_path, delimiter=';')

# Convertir la colonne 'Date' en format datetime pour une meilleure gestion des dates
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Mise en page de l'applicaation
app.layout = html.Div([
    html.H1("Évolution des Températures par Département", style={'textAlign': 'center'}),
    
    # Menu déroulant pour sélectionner le département
    dcc.Dropdown(
        id='departement-dropdown',
        options=[{'label': dept, 'value': dept} for dept in sorted(temperature_df['Département'].unique())],
        value=sorted(temperature_df['Département'].unique())[0],
        placeholder="Sélectionnez un département"
    ),
    
    # Graphique interactif
    dcc.Graph(id='temperature-histogram')
])

# Mise à jour du graphique en fonction du département sélectionné
@app.callback(
    Output('temperature-histogram', 'figure'),
    [Input('departement-dropdown', 'value')]
)
def update_histogram(selected_departement):
    # Filtrer les données en fonction du département sélectionné
    filtered_df = temperature_df[temperature_df['Département'] == selected_departement]
    
    # Calculer la température moyenne par date pour le département sélectionné
    daily_avg_temp = filtered_df.groupby('Date')['TMoy (°C)'].mean().reset_index()
    
    # Créer le graphique de l'évolution des températures
    graph = px.line(
        daily_avg_temp,
        x='Date',
        y='TMoy (°C)',
        title=f'Évolution des Températures - {selected_departement}',
        labels={'TMoy (°C)': 'Température Moyenne (°C)', 'Date': 'Date'},
        line_shape='linear'
    )

    graph.update_layout(
        xaxis_title='Date',
        yaxis_title='Température Moyenne (°C)',
        height=600
    )

    return graph

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True, port=8060)