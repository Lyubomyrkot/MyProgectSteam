import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bestSelling_games.csv')

difficult = df['difficulty'].value_counts()

difficult.plot(kind='pie', figsize=(10,6), autopct='%1.1f%%', legend = True, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0'])
plt.title("Яка складність ігор найпопулярніша у Steam?")
plt.show()