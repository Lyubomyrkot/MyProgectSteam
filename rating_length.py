import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bestSelling_games.csv')

plt.scatter(df['length'], df['rating'], color='skyblue')
cor = df[['length', 'rating']].corr()
print(cor)
plt.title("Чи залежить оцінка гри від її часу проведених в грі?")
plt.xlabel("Рейтинг проведення гри (години)")
plt.ylabel("Рейтинг гри")
plt.grid(True)
plt.show()