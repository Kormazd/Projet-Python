
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

file_path = 'Data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')

temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Évolution des Températures par Département", style={'textAlign': 'center'}),
    
    dcc.Dropdown(
        id='departement-dropdown',
        options=[{'label': dept, 'value': dept} for dept in sorted(temperature_df['Département'].unique())],
        value=sorted(temperature_df['Département'].unique())[0],
        placeholder="Sélectionnez un département"
    ),
    
    dcc.Graph(id='temperature-histogram')
])

@app.callback(
    Output('temperature-histogram', 'figure'),
    [Input('departement-dropdown', 'value')]
)
def update_histogram(selected_departement):
    filtered_df = temperature_df[temperature_df['Département'] == selected_departement]
    
    daily_avg_temp = filtered_df.groupby('Date')['TMoy (°C)'].mean().reset_index()
    
    fig = px.line(
        daily_avg_temp,
        x='Date',
        y='TMoy (°C)',
        title=f'Évolution des Températures - {selected_departement}',
        labels={'TMoy (°C)': 'Température Moyenne (°C)', 'Date': 'Date'},
        line_shape='linear'
    )

    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Température Moyenne (°C)',
        height=600
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port=8060)
