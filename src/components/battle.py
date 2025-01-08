import pandas as pd
from dash import dcc, html

# Chargement des données
file_path = 'data/raw/temperature-quotidienne-departementale.csv'
temperature_df = pd.read_csv(file_path, delimiter=';')
temperature_df['Date'] = pd.to_datetime(temperature_df['Date'])

def compare_departments(dept1, dept2, years):
    # Filtrer les données pour les deux départements et la période choisie
    end_date = temperature_df['Date'].max()
    start_date = end_date - pd.DateOffset(years=years)
    filtered_df = temperature_df[
        (temperature_df['Date'] >= start_date) & 
        (temperature_df['Date'] <= end_date) & 
        (temperature_df['Département'].isin([dept1, dept2]))
    ]

    # Calculer les statistiques
    result = {}
    for dept in [dept1, dept2]:
        dept_data = filtered_df[filtered_df['Département'] == dept]
        result[dept] = {
            'Température Moyenne': dept_data['TMoy (°C)'].mean(),
            'Température Max': dept_data['TMax (°C)'].max(),
            'Date Max': dept_data.loc[dept_data['TMax (°C)'].idxmax(), 'Date'],
            'Température Min': dept_data['TMin (°C)'].min(),
            'Date Min': dept_data.loc[dept_data['TMin (°C)'].idxmin(), 'Date'],
        }

    # Identifier le gagnant
    winner = max(result, key=lambda d: result[d]['Température Moyenne'])
    return result, winner

def update_battle(dept1, dept2, years):
    if dept1 and dept2 and dept1 != dept2:
        results, winner = compare_departments(dept1, dept2, years)
        return html.Div([
            html.H3(f"Comparaison sur {years} ans :"),
            html.Ul([
                html.Li(f"Département 1 ({dept1}) : Moyenne = {results[dept1]['Température Moyenne']:.2f}°C, "
                        f"Max = {results[dept1]['Température Max']}°C ({results[dept1]['Date Max']}), "
                        f"Min = {results[dept1]['Température Min']}°C ({results[dept1]['Date Min']})"),
                html.Li(f"Département 2 ({dept2}) : Moyenne = {results[dept2]['Température Moyenne']:.2f}°C, "
                        f"Max = {results[dept2]['Température Max']}°C ({results[dept2]['Date Max']}), "
                        f"Min = {results[dept2]['Température Min']}°C ({results[dept2]['Date Min']})"),
            ]),
            html.H4(f"Gagnant : {winner}")
        ])
    return html.Div("Veuillez sélectionner deux départements différents.")
