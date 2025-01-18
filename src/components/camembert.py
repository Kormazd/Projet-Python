import pandas as pd
import plotly.express as px

# Chargement des données depuis le fichier CSV
file_path = 'data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

def update_camembert(selected_date):
    """
    Génère un camembert montrant la répartition des températures moyennes pour une date donnée.

    Args:
        selected_date (str): La date sélectionnée (format ISO).

    Returns:
        plotly.graph_objects.Figure: Graphique en camembert représentant les intervalles de températures.
    """
    selected_date = pd.to_datetime(selected_date)

    # Filtrer les données pour la date sélectionnée
    filtered_df = temperature_df[temperature_df['Date'] == selected_date].copy()

    # Gestion du cas où aucune donnée n'est disponible
    if filtered_df.empty:
        fig = px.pie(
            names=["Aucune donnée"],
            values=[1],
            title=f"Aucune donnée pour la date {selected_date.strftime('%Y-%m-%d')}"
        )
        fig.update_layout(
            autosize=True,
            margin=dict(l=20, r=20, t=40, b=40),
            hoverlabel=dict(bgcolor="#444444")
        )
        return fig

    # Calcul des intervalles de température
    min_temp = int(filtered_df['TMoy (°C)'].min()) - 1
    max_temp = int(filtered_df['TMoy (°C)'].max()) + 1
    bins = range(min_temp, max_temp + 2, 2)
    filtered_df['temp_bin'] = pd.cut(filtered_df['TMoy (°C)'], bins=bins, right=False)
    filtered_df['temp_bin_str'] = filtered_df['temp_bin'].apply(lambda i: f"{int(i.left)}~{int(i.right)} °C")
    temp_counts = filtered_df['temp_bin_str'].value_counts(normalize=True).reset_index()
    temp_counts.columns = ['Intervalle de Température (°C)', 'Proportion']

    # Création du graphique en camembert
    fig = px.pie(
        temp_counts,
        values='Proportion',
        names='Intervalle de Température (°C)'
    )

    # Configuration des options de mise en page
    fig.update_traces(
        hovertemplate=(
            "<b>🌡️ Temp. : </b>%{label}<br>"
            "<b>📊 Prop. : </b>%{percent:.1%}"
        )
    )
    
    fig.update_layout(
        autosize=True,
        margin=dict(l=5, r=5, t=10, b=10),
        hoverlabel=dict(bgcolor="#444444")
    )

    return fig
