import pandas as pd

df = pd.read_csv('input.csv')

odd = df.iloc[::2]
even = df.iloc[1::2]

odd.to_csv('odd.csv', index=False)
even.to_csv('even.csv', index=False)
