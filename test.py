import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv("data.csv")

#IT = INFORMASIYA TEXNOLOGIYALARI
#IS = INFORMASIYA TEHLUKESIZLIYI
#KM = KOMPUTER MUHENDISLIYI
#KE = KOMPUTER ELMLERI
istenen_ixtisas = input("bir ixtisas adı girin: (IT),(IS),(KM).(KE) :")

filtered_data = df[df['Ixtisas'] == istenen_ixtisas]

plt.figure(figsize=(12, 6)) 
for universite in filtered_data['Uni'].unique():
    data_by_universite = filtered_data[filtered_data['Uni'] == universite]
    plt.plot(data_by_universite['Tarix'], data_by_universite['Bal'], marker='o', label=universite)

plt.xlabel('IL')
plt.ylabel('Ortalama Bal ')
plt.title(f"{istenen_ixtisas} İxtisasının Üniversitetlere Göre Ortalama Bal Değerleri")
plt.legend()
plt.grid(True)

plt.xticks(rotation=45)  
universiteler = filtered_data['Uni'].unique()
x_2024 = 2024
y_2024_texminleri = []
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

for i , universite in enumerate(universiteler):
    data_by_universite = filtered_data[filtered_data['Uni'] == universite]
    slope, intercept, _, _, _ = linregress(data_by_universite['Tarix'], data_by_universite['Bal'])
    y_2024_texmini = slope * x_2024 + intercept
    y_2024_texminleri.append(y_2024_texmini)
    color = colors[i % len(colors)]

    plt.axhline(y=y_2024_texmini, color=color, linestyle='--', label=f'{universite} (2024 Praqnozu)')

plt.legend()
plt.tight_layout()  

plt.show()
plt.savefig(f'{istenen_ixtisas}_ixtisas.png')  

for i, universite in enumerate(universiteler):
    print(f"{universite} üniversitetindeki texmini ortalama bal değeri (2024): {y_2024_texminleri[i]:.2f}")
