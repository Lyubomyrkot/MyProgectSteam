import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bestSelling_games.csv')

plt.scatter(df['length'], df['rating'], color='skyblue')

plt.title("Чи залежить оцінка гри від її складності?")
plt.xlabel("Рейтинг складності")
plt.ylabel("Рейтинг гри")
plt.grid(True)
plt.show()
print(df['length'].corr(df['rating']))