import pandas as pd
df = pd.read_csv('avocado.csv')
d, s = list(df['AveragePrice']), list(df['Date'])
data_pice = dict(zip(df['Date'], df['AveragePrice'] ))
print(data_pice)
