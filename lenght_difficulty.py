import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bestSelling_games.csv')

plt.scatter(df['length'], df['difficulty'], color='skyblue')
cor = df[['length', 'difficulty']].corr()
print(cor)
plt.title("Чи залежить час проведений в грі від складності?")
plt.xlabel("Рейтинг проведення гри (години)")
plt.ylabel("Складність гри")
plt.grid(True)
plt.show()