import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

file_path = 'data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

def update_histogram(selected_departement):
    filtered_df = temperature_df[temperature_df['Département'] == selected_departement]
    daily_avg_temp = filtered_df.groupby('Date')['TMoy (°C)'].mean().reset_index()
    
    fig = px.line(
        daily_avg_temp,
        x='Date',
        y='TMoy (°C)',
        labels={'TMoy (°C)': 'Température Moyenne (°C)', 'Date': 'Date'},
        line_shape='linear'
    )
    
    # Ajustement dynamique avec une hauteur minimum pour éviter les sauts de taille trop brusques
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Température Moyenne (°C)',
        autosize=True,
        height=max(500, min(900, len(daily_avg_temp) * 10)),  # Hauteur dynamique entre 500px et 900px
        margin=dict(l=20, r=20, t=40, b=40)
    )
    return fig
