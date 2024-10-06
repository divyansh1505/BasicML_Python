import pandas as pd
import matplotlib.pyplot as plt

fifa = pd.read_csv("fifa_data.csv")

# print(fifa.head(10))
# print(fifa.describe())
# print(fifa.columns)

left = fifa.loc(fifa['Preferred Foot'=='Left']).count()[0]
right = fifa.loc(fifa['Preferred Foot'=='Right']).count()[0]

labels = ('Left', 'Right')

plt.pie([left, right], labels=labels)

plt.show()