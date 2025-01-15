import pandas as pd
import json
import plotly.express as px

MAP_HEIGHT = 500
MAP_WIDTH = 500

file_path = 'data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])
temperature_df = temperature_df.dropna(subset=['TMoy (°C)'])
temperature_df = temperature_df.rename(columns={"Code INSEE département": "Code_INSEE"})
temperature_df['Code_INSEE'] = temperature_df['Code_INSEE'].astype(str)

with open("data/raw/departements-version-simplifiee.geojson", 'r', encoding='utf-8') as f:
    geojson_data = json.load(f)

def update_map(selected_date):
    selected_date = pd.to_datetime(selected_date) if selected_date else temperature_df['Date'].min()
    filtered_df = temperature_df[temperature_df['Date'] == selected_date]
    
    custom_colorscale = [
        [0, "#315D8A"],   # Froid (bleu)
        [0.45, "#ADCFE4"],
        [0.5, "#F0F0F0"],
        [0.55, "#FEA694"],
        [1, "#DF3A41"]    # Chaud (rouge)
    ]

    fig = px.choropleth_mapbox(
        filtered_df,
        geojson=geojson_data,
        locations='Code_INSEE',
        featureidkey='properties.code',
        color='TMoy (°C)',
        mapbox_style="carto-positron",
        color_continuous_scale=custom_colorscale,
        zoom=4.2,
        center={"lat": 46.603354, "lon": 2.5},
        hover_data={'Département': True, 'TMoy (°C)': ':.1f', 'TMin (°C)': ':.1f', 'TMax (°C)': ':.1f'}
    )
    fig.update_traces(
        hovertemplate=(
            "<u><b>%{customdata[0]}</b></u><br>"
            "<b>🌡️ Moy. :</b> %{customdata[1]:.1f}°C<br>"
            "<b>🌡️ Min. :</b> %{customdata[2]:.1f}°C<br>"
            "<b>🌡️ Max. :</b> %{customdata[3]:.1f}°C<extra></extra>"
        )
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=40),
        height=MAP_HEIGHT,
        width=MAP_WIDTH,
        hoverlabel=dict(bgcolor="#444444"),
        coloraxis_colorbar=dict(
            orientation='h',
            title="Temp. (°C)",
            x=0.5,
            xanchor='center',
            y=-0.15,
            yanchor='top'
        )
    )
    return fig
