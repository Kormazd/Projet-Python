import pandas as pd
import plotly.express as px

file_path = 'data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

def update_histogram(selected_departement):
    filtered_df = temperature_df[temperature_df['Département'] == selected_departement]
    fig = px.histogram(
        filtered_df,
        x='TMoy (°C)',
        nbins=20,
        labels={'TMoy (°C)': 'Température Moyenne (°C)', 'count': 'Nombre de Jours'},
    )
    fig.update_traces(
        hovertemplate=(
            "<b>🌡️ Temp. :</b> %{x:.1f}°C<br>"
            "<b>🔆 Nbr. jours:</b> %{y}<extra></extra>"
        )
    )
    fig.update_layout(
        xaxis_title='Température Moyenne (°C)',
        yaxis_title='Nombre de Jours',
        autosize=True,  # <-- Ajout
        margin=dict(l=5, r=5, t=10, b=10),
        hoverlabel=dict(bgcolor="#444444")
    )

    return fig
