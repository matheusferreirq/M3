import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
# Utiliza a função read_csv do pandas para ler o arquivo 'medical_examination.csv' e atribui-o a um DataFrame na variável df
df = pd.read_csv('medical_examination.csv')

# 2
# Cria a coluna 'overweight' dividindo o peso pela altura ao quadrado e atribuindo 1 se o valor for maior que 25 ou 0 se for menor ou igual
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3
# Normaliza os dados de 'cholesterol' e 'gluc', atribuindo 0 se o valor for 1 e 1 se for maior que 1
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
# Define a função draw_cat_plot
def draw_cat_plot():
    # 5
    # Utiliza a função 'melt' para empilhar as colunas do df menos 'cardio' e criando um DataFrame longo
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    # Agrupa por cardio, variable e value
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])

    # Conta as ocorrências de cada grupo
    df_cat = df_cat.size()

    # 7 e 8
    # Reseta o índice para transformar o Series em DataFrame e converte os dados em formato "longo" novamente
    df_cat = df_cat.reset_index(name='total')

    # Cria o gráfico de barras com seaborn
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
# Define a função draw_heat_map
def draw_heat_map():
    # 11

    # Filtra os dados onde 'ap_lo' é menor ou igual a 'ap_hi'
    df_heat = df[df['ap_lo'] <= df['ap_hi']]

    # Filtra os valores de 'height' e 'weight' para remover os 2.5% inferiores e superiores
    df_heat = df_heat[(df_heat['height'] >= df_heat['height'].quantile(0.025)) & (df_heat['height'] <= df_heat['height'].quantile(0.975))]
    df_heat = df_heat[(df_heat['weight'] >= df_heat['weight'].quantile(0.025)) & (df_heat['weight'] <= df_heat['weight'].quantile(0.975))]

    # 12
    # Mostra como as variáveis estão correlacionadas entre si
    corr = df_heat.corr()

    # 13
    # Cria uma máscara para o triângulo superior da matriz de correlação
    mask = np.triu(np.ones_like(corr))

    # 14
    # Cria a figura e o eixo para o heatmap
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    # Desenha o heatmap a partir da matriz de correlação
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", square=True, cbar_kws={'shrink': 0.5}, ax=ax)

    # 16
    fig.savefig('heatmap.png')
    return fig