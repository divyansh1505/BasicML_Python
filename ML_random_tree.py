# The random forest uses many trees, and it makes a prediction by 
# averaging the predictions of each component tree. It generally has 
# much better predictive accuracy than a single decision tree and it 
# works well with default parameters. If you keep modeling, you can 
# learn more models with even better performance, but many of those 
# are sensitive to getting the right parameters. 

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

lap_filepath = 'data.csv'
lap_data = pd.read_csv(lap_filepath)

y = lap_data['Price_euros']

lap_features = ['Company', 'Product', 'Screen', 'IPSpanel', 'RetinaDisplay', 
                'CPU_company', 'CPU_freq', 'CPU_model', 'GPU_company', 'GPU_model']

X = lap_data[lap_features]

X = pd.get_dummies(X, drop_first=True)
print(X.describe())

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
laptop_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, laptop_preds))

values = lap_data['Price_euros']
labels = lap_data['Company']

bars = plt.bar(labels, values)

plt.show()