import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bestSelling_games.csv')
#df.info()
#print(df.describe())
#df['supported_os'].value_counts().plot(kind='barh', legend=True, color=['skyblue'], figsize=(10, 6))
#

#temp = df[df['supported_os'] == 'win']['price'].max()
#temp = df[df['age_restriction'] <= 10 ]['price'].max()
#temp = df.groupby('supported_os')['rating'].agg(['min', 'max', 'mean'])
temp = df[df['supported_languages'] == 'English'].groupby('supported_os')['price'].agg(['min', 'max', 'mean'])
print(temp)
temp.plot(kind='barh', figsize=(10, 6), color=['skyblue', 'lightgreen', 'salmon'])
plt.show()