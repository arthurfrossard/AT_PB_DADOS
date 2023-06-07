import sqlite3
import pandas as pd

# Etapa 3:

# Item 9:
conn = sqlite3.connect('PB_Housing_Data.db')
df = pd.read_sql_query("SELECT * FROM Amostra_PB_Housing_Data", conn)
conn.close()
lot_area = 'Lot_Area'
lot_shape = 'Lot_Shape'

# Item 10:
print('Item 10 - Conteudo das duas variáveis:')
print(df[[lot_shape, lot_area]])

# Item 11:
print('\nItem 11 - Valores máximo, mínimo e a média:')
print(f'Valor máximo: {df[lot_area].max()}')
print(f'Valor mínimo: {df[lot_area].min()}')
print(f'Média: {round(df[lot_area].mean(),2)}')

# Item 12:
print('\nItem 12 - Listagem de itens únicos:')
print(df[lot_shape].unique())

# Etapa 4:

# Item 13:
list_lot_area = df[lot_area].tolist()

# Item 14:
list_lot_shape = df[lot_shape].tolist()

# Item 15:
soma_area = 0
for area in list_lot_area:
    if area > df[lot_area].mean():
        soma_area += area
print('\nItem 15 - Somas acima da média:')
print(f'Soma das areas dos lotes que estão acima da média: {soma_area}')

# Item 16:
print('\nItem 16 - Função de contagem de ocorrência:')


def contar_ocorrencias(lista):
    ocorrencias = {}
    for item in lista:
        if item in ocorrencias:
            ocorrencias[item] += 1
        else:
            ocorrencias[item] = 1
    return ocorrencias


for item, quantidade in contar_ocorrencias(list_lot_shape).items():
    print(f"{item}: {quantidade}")