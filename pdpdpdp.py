import pandas as pd

df = pd.read_csv('pokemon_data.csv')

h = df.columns
#print(h)

#if u wanna read each row

# if you wanna find specific data use loc()

#e = df.loc[df['Type 1'] == 'Grass']
#you can sort values 

#if u wanna delete column use drop('delete column')

#e = df.loc[df['Type 1'] == 'Fire','Type 1'] = 'flamer'

#df.groupby(['Type 1']).mean().sort_values('Defence')


print(df)