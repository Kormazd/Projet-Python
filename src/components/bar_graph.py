import pandas as pd
import plotly.express as px

# Chargement des données depuis le fichier CSV
file_path = 'data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

def update_bargraph(selected_departement):
    """
    Génère le graphique des températures moyennes pour un département donné.

    Args:
        selected_departement (str): Le département sélectionné.

    Returns:
        plotly.graph_objects.Figure: Graphique de type ligne avec les températures moyennes journalières.
    """
    # Filtrer les données pour le département sélectionné
    filtered_df = temperature_df[temperature_df['Département'] == selected_departement]
    daily_avg_temp = filtered_df.groupby('Date')['TMoy (°C)'].mean().reset_index()

    # Création du graphique
    fig = px.line(
        daily_avg_temp,
        x='Date',
        y='TMoy (°C)',
        labels={'TMoy (°C)': 'Température Moyenne (°C)', 'Date': 'Date'},
        line_shape='linear'
    )

    # Configuration des options de mise en page
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Température Moyenne (°C)',
        autosize=True,
        margin=dict(l=5, r=5, t=10, b=10),
        xaxis=dict(tickformat='%d %b. %Y'),
        hoverlabel=dict(bgcolor="#444444")
    )

    # Personnalisation des bulles d'information
    fig.update_traces(
        hovertemplate=(
            "<b>📅 Date :</b> %{x|%d %b. %Y}<br>"
            "<b>🌡️ Temp. :</b> %{y:.1f}°C<extra></extra>"
        )
    )

    return fig
