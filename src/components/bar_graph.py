import pandas as pd
import plotly.express as px

BARG_HEIGHT = 400
BARG_WIDTH = 550

file_path = 'data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

def update_bargraph(selected_departement):
    filtered_df = temperature_df[temperature_df['Département'] == selected_departement]
    daily_avg_temp = filtered_df.groupby('Date')['TMoy (°C)'].mean().reset_index()
    fig = px.line(
        daily_avg_temp,
        x='Date',
        y='TMoy (°C)',
        labels={'TMoy (°C)': 'Température Moyenne (°C)', 'Date': 'Date'},
        line_shape='linear'
    )
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Température Moyenne (°C)',
        autosize=True,
        height=BARG_HEIGHT,
        width=BARG_WIDTH,
        margin=dict(l=20, r=20, t=40, b=40),
        xaxis=dict(tickformat='%d %b. %Y'),
        hoverlabel=dict(bgcolor="#444444")
    )
    fig.update_traces(
        hovertemplate=(
            "<b>📅 Date :</b> %{x|%d %b. %Y}<br>"
            "<b>🌡️ Temp. :</b> %{y:.1f}°C<extra></extra>"
        )
    )
    return fig
