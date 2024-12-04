import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import json

# Charger les données de température
temperature_df = pd.read_csv('data/raw/temperature-quotidienne-departementale.csv', delimiter=';')

# Préparer les données
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])
temperature_df = temperature_df.dropna(subset=['TMoy (°C)'])  # Retirer les lignes avec valeurs manquantes
temperature_df = temperature_df.rename(columns={"Code INSEE département": "Code_INSEE"})  # Harmoniser les noms
temperature_df['Code_INSEE'] = temperature_df['Code_INSEE'].astype(str)

# Charger les données géographiques (GeoJSON)
with open("data/raw/departements-version-simplifiee.geojson", 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Mise en page de l'application
app.layout = html.Div([
    html.H1("Carte des Températures en France", style={'textAlign': 'center'}),
    dcc.DatePickerSingle(
        id='date-picker',
        min_date_allowed=temperature_df['Date'].min().date(),
        max_date_allowed=temperature_df['Date'].max().date(),
        initial_visible_month=temperature_df['Date'].min().date(),
        date=temperature_df['Date'].min().date()
    ),
    dcc.Graph(id='temperature-map')
])

# Callback pour mettre à jour la carte
@app.callback(
    Output('temperature-map', 'figure'),
    [Input('date-picker', 'date')]
)
def update_map(selected_date):
    selected_date = pd.to_datetime(selected_date) if selected_date else temperature_df['Date'].min()
    filtered_df = temperature_df[temperature_df['Date'] == selected_date]

    fig = px.choropleth_mapbox(
        filtered_df,
        geojson=geojson_data,
        locations='Code_INSEE',  # Identifier les départements
        featureidkey='properties.code',  # Correspondance avec le code géographique
        color='TMoy (°C)',  # Coloration selon la température moyenne
        color_continuous_scale="thermal",
        mapbox_style="carto-positron",
        zoom=4.7,
        center={"lat": 46.603354, "lon": 1.888334},
        hover_data={'TMoy (°C)': ':.1f', 'TMin (°C)': ':.1f', 'TMax (°C)': ':.1f'}
    )

    fig.update_layout(
        title=f"Températures au {selected_date.strftime('%Y-%m-%d')}",
        margin={"r": 0, "t": 50, "l": 0, "b": 0},
        height=600
    )
    return fig

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True, port=8060)
