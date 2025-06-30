import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bestSelling_games.csv')

tags = df['supported_languages'].str.split(',').explode().str.strip().str.lower()

tag_counts = tags.value_counts().head(10)

tag_counts.plot(kind='barh', figsize=(10,6), color='orange')
plt.title("ТОП 10 найпопулярніших мов що підтримуються в ігорах у Steam")
plt.gca().invert_yaxis()
plt.show()