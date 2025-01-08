import pandas as pd
import plotly.express as px

HISTOGRAM_HEIGHT = 400
HISTOGRAM_WIDTH = 550  

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

    fig.update_layout(
        xaxis_title='Température Moyenne (°C)',
        yaxis_title='Nombre de Jours',
        height=HISTOGRAM_HEIGHT,
        width=HISTOGRAM_WIDTH,
        margin=dict(l=20, r=20, t=40, b=40)
    )
    return fig
