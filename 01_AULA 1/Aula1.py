# -*- coding: utf-8 -*-
"""Exemplo1.1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s-5JVPNkrMChSZ-dSO64O0NhCGSL5qHc

# Python para Data Science ⛹
# Msc. Ailton Santos

Exemplo 1:

Você tem os registros de vendas diárias de um produto específico durante um mês. Seu objetivo é entender melhor o comportamento dessas vendas usando medidas estatísticas básicas.
"""

import statistics as st

# Geração dos Dados
vendas_diarias = [
    120.5, 130.2, 115.8, 122.0, 135.0, 126.7, 129.1, 131.4,
    125.5, 133.2, 116.5, 125.0, 136.0, 126.7, 129.1, 135.4,
    128.5, 135.2, 116.8, 120.0, 135.0, 126.7, 126.1, 130.5,
]

print ('--- Dados Simulados ----')
print ('Vendas Diárias', vendas_diarias)
print ('\n')

print('Analise Descitiva Simples')

tamanho_amostra = len(vendas_diarias)

print('Qtde de dias de vendas', {tamanho_amostra})

media_vendas = st.mean(vendas_diarias)
print(media_vendas)

mediana_vendas = st.median(vendas_diarias)
print(mediana_vendas)

moda_vendas = st.mode(vendas_diarias)
print (f'Moda das vendas',{moda_vendas})

# Moda
try:
  moda_vendas = st.mode(vendas_diarias)
  print (f'Moda das vendas',{moda_vendas})
except st.StatisticsError as e:
  print('Não foi possivel calcula r a moda (erro: {a})')

desvio_padrao = st.stdev(vendas_diarias)
print (desvio_padrao)

variancia_vendas=st.variance(vendas_diarias)
print(variancia_vendas)

min_vendas = min(vendas_diarias)
print(min_vendas)

max_vendas = max(vendas_diarias)
print(max_vendas)