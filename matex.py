import pandas as pd 
import matplotlib.pyplot as plt

gas = pd.read_csv('gas_prices.csv')

# print(gas.head())

x = gas.Year
y= gas.USA

x2 = gas.Year
y2 = gas.Canada

x3 = gas.Year
y3 = gas.Italy

x4 = gas.Year
y4 = gas.Mexico 

x5 = gas.Year
y5 = gas.France

x6 = gas.Year
y6 = gas.Japan

plt.xlabel('Year')
plt.ylabel('USD per Gallon')
plt.title('Gas prices over time')

plt.plot(x, y, label='USA', marker='.')
plt.plot(x2, y2, label='Canada', marker='.')
plt.plot(x3, y3, label='Italy', marker='.')
plt.plot(x4, y4, label='Mexico', marker='.')
plt.plot(x5, y5, label='France', marker='.')
plt.plot(x6, y6, label='Japan', marker='.')

plt.xticks(x[::3])
#Another way to plot many values :
#countries_to_plot = ['USA', 'Canada', 'Italy', 'Mexico', 'France', 'Japan']
#for country in gas: 
#    if country in counties_to_plot
#         plt.plot(gas.Year, gas[country], marker='.')

plt.legend()
plt.savefig("gas_price.png", dpi=1500)
plt.show()