import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Load the dataset
lap_filepath = 'data.csv'
lap_data = pd.read_csv(lap_filepath)

# Display the columns
print(lap_data.columns)

# Target variable, WHAT WE WANT TO PREDICT
y = lap_data['Price_euros']
print(y.head())

# Features to use for training the model, WE USED THESE DATA TO TRAIN THE MODEL TO PREDICT PRICES
lap_features = ['Company', 'Product', 'Screen', 'IPSpanel', 'RetinaDisplay', 
                'CPU_company', 'CPU_freq', 'CPU_model', 'GPU_company', 'GPU_model']

# Check if features need encoding
X = lap_data[lap_features]

# Convert categorical features to numerical using one-hot encoding (if necessary)
X = pd.get_dummies(X, drop_first=True)

print(X.describe())

# Initialize and fit the model
laptop_model = DecisionTreeRegressor(random_state=1)
laptop_model.fit(X, y)

# Display some predictions
print(X.head())
print(laptop_model.predict(X.head()))

