import pandas as pd

df = pd.read_excel('Practica for students.xlsx')

data = [
    'DATE',
    'month',
    '№',
    'Year',
    'Code',
    "Surname"
    
]

new_df = df[data]
new_df['month'] = new_df['month'].str.replace(r"$",'')