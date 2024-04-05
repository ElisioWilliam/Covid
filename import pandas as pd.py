import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

total_casos_2021 = 10881168
total_casos_2024 = 518972  
novos_obitos_2021 = 323117  
novos_obitos_2024 = 2611  

anos = ['2021', '2024']
total_casos = [total_casos_2021, total_casos_2024]
novos_obitos = [novos_obitos_2021, novos_obitos_2024]

plt.figure(figsize=(12, 6))
bar_width = 0.35
plt.bar(anos, total_casos, bar_width, label='Total de Casos', color='b')
plt.bar([x + bar_width for x in range(len(anos))], novos_obitos, bar_width, label='Novos Óbitos', color='r')
plt.xlabel('Ano')
plt.ylabel('Quantidade')
plt.title('Comparação do Total de Casos de COVID-19 e Novos Óbitos no Brasil (Primeiros 5 Meses)')
plt.legend()

plt.savefig('grafico_comparacao_casos_obitos_covid.png')

plt.show()
