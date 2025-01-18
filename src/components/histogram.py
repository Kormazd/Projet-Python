import pandas as pd
import plotly.express as px

# Chargement des données depuis le fichier CSV
file_path = 'data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

def update_histogram(selected_departement):
    """
    Génère un histogramme des températures moyennes pour un département donné.

    Args:
        selected_departement (str): Le département sélectionné.

    Returns:
        plotly.graph_objects.Figure: Histogramme montrant la distribution des températures moyennes.
    """
    # Filtrer les données pour le département sélectionné
    filtered_df = temperature_df[temperature_df['Département'] == selected_departement]

    # Création de l'histogramme
    fig = px.histogram(
        filtered_df,
        x='TMoy (°C)',
        nbins=20,
        labels={'TMoy (°C)': 'Température Moyenne (°C)', 'count': 'Nombre de Jours'}
    )

    # Personnalisation des bulles d'information (hover)
    fig.update_traces(
        hovertemplate=(
            "<b>🌡️ Temp. :</b> %{x:.1f}°C<br>"
            "<b>🔆 Nbr. jours:</b> %{y}<extra></extra>"
        )
    )

    # Configuration des options de mise en page
    fig.update_layout(
        xaxis_title='Température Moyenne (°C)',
        yaxis_title='Nombre de Jours',
        autosize=True,
        margin=dict(l=5, r=5, t=10, b=10),
        hoverlabel=dict(bgcolor="#444444")
    )

    return fig
