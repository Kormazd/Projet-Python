# src/components/pie_chart.py
import pandas as pd
import plotly.express as px

HISTOGRAM_HEIGHT = 400
HISTOGRAM_WIDTH = 550

file_path = 'data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

PIECHART_HEIGHT = 600

def update_pie_chart(selected_date):
    filtered_df = temperature_df[temperature_df['Date'] == pd.Timestamp(selected_date)]
    temp_counts = filtered_df['TMoy (°C)'].value_counts(normalize=True).reset_index()
    temp_counts.columns = ['Température (°C)', 'Proportion']
    
    fig = px.pie(
        temp_counts,
        values='Proportion',
        names='Température (°C)',
        title=f"Répartition des températures pour la date {selected_date}",
    )
    fig.update_layout(
        height=PIECHART_HEIGHT,
        margin=dict(l=20, r=20, t=40, b=40)
    )
    return fig
