import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_2024 = pd.read_csv('"C:\\Users\\elisi\\Downloads\\Covid\\dados_covid_2024.csv"')
dados_2021 = pd.read_csv('"C:\\Users\\elisi\\Downloads\\Covid\\dados_covid_2021.csv"')

dados_2024_primeiro_semestre = dados_2024[dados_2024['data'].str.startswith('2024-01') | 
                                          dados_2024['data'].str.startswith('2024-02') |
                                          dados_2024['data'].str.startswith('2024-03') |
                                          dados_2024['data'].str.startswith('2024-04') |
                                          dados_2024['data'].str.startswith('2024-05')]

dados_2021_primeiro_semestre = dados_2021[dados_2021['data'].str.startswith('2021-01') | 
                                          dados_2021['data'].str.startswith('2021-02') |
                                          dados_2021['data'].str.startswith('2021-03') |
                                          dados_2021['data'].str.startswith('2021-04') |
                                          dados_2021['data'].str.startswith('2021-05')]

total_casos_2024 = dados_2024_primeiro_semestre['casosAcumulado'].sum()
total_mortes_2024 = dados_2024_primeiro_semestre['obitosAcumulado'].sum()

total_casos_2021 = dados_2021_primeiro_semestre['casosAcumulado'].sum()
total_mortes_2021 = dados_2021_primeiro_semestre['obitosAcumulado'].sum()

dados_comparativos = pd.DataFrame({
    'Ano': ['2021', '2024'],
    'Total de Casos': [total_casos_2021, total_casos_2024],
    'Total de Mortes': [total_mortes_2021, total_mortes_2024]
})

plt.figure(figsize=(10, 6))
sns.barplot(data=dados_comparativos, x='Ano', y='Total de Casos', palette='Blues')
plt.title('Comparação do Total de Casos de COVID-19 no Brasil (Primeiro Semestre)')
plt.ylabel('Total de Casos')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=dados_comparativos, x='Ano', y='Total de Mortes', palette='Reds')
plt.title('Comparação do Total de Mortes por COVID-19 no Brasil (Primeiro Semestre)')
plt.ylabel('Total de Mortes')
plt.show()
