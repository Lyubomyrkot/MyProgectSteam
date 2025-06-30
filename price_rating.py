import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bestSelling_games.csv')

plt.scatter(df['price'], df['rating'], color='skyblue')
cor = df[['price', 'rating']].corr()
print(cor)
plt.title("Чи залежить ціна гри від оцінки гри?")
plt.xlabel("Ціна гри")
plt.ylabel("Рейтинг гри")
plt.grid(True)
plt.show()