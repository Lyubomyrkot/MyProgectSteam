import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bestSelling_games.csv')

# Витягуємо всі теги в один список
tags = df['user_defined_tags'].str.split(',').explode().str.strip().str.lower()

# Рахуємо найпопулярніші теги
tag_counts = tags.value_counts().head(10)

# Побудова графіка
tag_counts.plot(kind='barh', figsize=(10,6), color='orange')
plt.title("ТОП 10 найпопулярніших тегів ігор у Steam")
plt.xlabel("Кількість ігор з таким тегом")
plt.gca().invert_yaxis()  # Щоб найпопулярніші були зверху
plt.show()