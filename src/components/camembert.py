import pandas as pd
import plotly.express as px

file_path = 'data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

PIECHART_HEIGHT = 600

def update_camembert(selected_date):
    """
    Renvoie un camembert représentant la répartition des températures par tranches de 2°C 
    pour la date sélectionnée.
    """
    selected_date = pd.to_datetime(selected_date)
    filtered_df = temperature_df[temperature_df['Date'] == selected_date]
    
    if filtered_df.empty:
        fig = px.pie(
            names=["Aucune donnée"],
            values=[1],
            title=f"Aucune donnée pour la date {selected_date.strftime('%Y-%m-%d')}"
        )
        return fig

    min_temp = int(filtered_df['TMoy (°C)'].min()) - 1
    max_temp = int(filtered_df['TMoy (°C)'].max()) + 1
    bins = range(min_temp, max_temp + 2, 2)
    filtered_df['temp_bin'] = pd.cut(filtered_df['TMoy (°C)'], bins=bins, right=False)
    filtered_df['temp_bin_str'] = filtered_df['temp_bin'].astype(str)
    temp_counts = filtered_df['temp_bin_str'].value_counts(normalize=True).reset_index()
    temp_counts.columns = ['Intervalle de Température (°C)', 'Proportion']
    fig = px.pie(
        temp_counts,
        values='Proportion',
        names='Intervalle de Température (°C)',
        title=f"Répartition des températures (par tranches de 2°C) pour la date {selected_date.strftime('%Y-%m-%d')}",
    )
    fig.update_layout(
        height=PIECHART_HEIGHT,
        margin=dict(l=20, r=20, t=40, b=40)
    )
    return fig
