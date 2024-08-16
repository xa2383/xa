import pandas as pd
diamonds=pd.read_csv(‘first.csv’)
print("First 5 rows:")
print(diamonds.head())
print(" Last 5 lines:")
print(diamonds.tail())