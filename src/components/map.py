import pandas as pd
import json
import plotly.express as px

# Chargement des données et géométrie
file_path = 'data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])
temperature_df = temperature_df.dropna(subset=['TMoy (°C)'])
temperature_df = temperature_df.rename(columns={"Code INSEE département": "Code_INSEE"})
temperature_df['Code_INSEE'] = temperature_df['Code_INSEE'].astype(str)

# Chargement des données géographiques (GeoJSON)
with open("data/raw/departements-version-simplifiee.geojson", 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

def update_map(selected_date):
    """
    Génère une carte choroplèthe montrant les températures moyennes par département pour une date donnée.

    Args:
        selected_date (str): La date sélectionnée (format ISO).

    Returns:
        plotly.graph_objects.Figure: Carte affichant les températures moyennes par département.
    """
    selected_date = pd.to_datetime(selected_date) if selected_date else temperature_df['Date'].min()

    # Filtrer les données pour la date sélectionnée
    filtered_df = temperature_df[temperature_df['Date'] == selected_date]

    # Création de la carte
    fig = px.choropleth_mapbox(
        filtered_df,
        geojson=geojson_data,
        locations='Code_INSEE',
        featureidkey='properties.code',
        color='TMoy (°C)',
        mapbox_style="carto-positron",
        color_continuous_scale=[
            [0, "#315D8A"], [0.45, "#ADCFE4"], [0.5, "#F0F0F0"], [0.55, "#FEA694"], [1, "#DF3A41"]
        ],
        zoom=3.9,
        center={"lat": 46.603354, "lon": 2.5},
        hover_data={'Département': True, 'TMoy (°C)': ':.1f', 'TMin (°C)': ':.1f', 'TMax (°C)': ':.1f'}
    )

    # Personnalisation des bulles d'information (hover)
    fig.update_traces(
        hovertemplate=(
            "<u><b>%{customdata[0]}</b></u><br>"
            "<b>🌡️ Moy. :</b> %{customdata[1]:.1f}°C<br>"
            "<b>🌡️ Min. :</b> %{customdata[2]:.1f}°C<br>"
            "<b>🌡️ Max. :</b> %{customdata[3]:.1f}°C<extra></extra>"
        )
    )

    # Configuration des options de mise en page
    fig.update_layout(
        autosize=True,
        margin=dict(l=5, r=5, t=10, b=10),
        hoverlabel=dict(bgcolor="#444444")
    )

    return fig
