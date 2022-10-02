import pandas as pd

index = [('California',2000),('California',2010),
         ('Rome',2000),('Rome',2010)
         ('Yakutza',2000),('Yakutza',2010)
         
         ]

populations = [1234,234,234,1232,312,54]
p = pd.Series(populations, index= index)
index = pd.MultiIndex.from_tuples(index)
p = p.reindex(index)
print(index)