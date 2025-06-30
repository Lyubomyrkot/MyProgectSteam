import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bestSelling_games.csv')

tags = df['user_defined_tags'].str.split(',').explode().str.strip().str.lower()

tag_counts = tags.value_counts().head(10)

tag_counts.plot(kind='barh', figsize=(10,6), color='#72fca0')
plt.title("ТОП 10 найпопулярніших тегів ігор у Steam")
plt.xlabel("Кількість ігор з таким тегом")
plt.gca().invert_yaxis()
plt.show()