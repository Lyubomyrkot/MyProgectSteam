import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bestSelling_games.csv')

plt.scatter(df['price'], df['difficulty'], color='skyblue')
cor = df[['price', 'difficulty']].corr()
print(cor)
plt.title("Чи залежить ціна гри від складності?")
plt.xlabel("Ціна гри")
plt.ylabel("Складність гри")
plt.grid(True)
plt.show()