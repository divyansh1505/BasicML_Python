import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Load the dataset
lap_filepath = '/home/divyansh1505/Desktop/archive./data.csv'
lap_data = pd.read_csv(lap_filepath)

# Display the columns
print(lap_data.columns)

# Target variable, WHAT WE WANT TO PREDICT
y = lap_data['Price_euros']
print(y.head())

# Features to use for training the model
lap_features = ['Company', 'Product', 'Screen', 'IPSpanel', 'RetinaDisplay', 
                'CPU_company', 'CPU_freq', 'CPU_model', 'GPU_company', 'GPU_model']

# Check if features need encoding
X = lap_data[lap_features]

# Convert categorical features to numerical using one-hot encoding
X = pd.get_dummies(X, drop_first=True)

print(X.describe())

# Split the data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# Define the custom get_mae function
def get_mae(model, train_X, train_y, val_X, val_y):
    # Fit the model
    model.fit(train_X, train_y)
    
    # Make predictions on validation set
    val_predictions = model.predict(val_X)
    
    # Calculate Mean Absolute Error
    mae = mean_absolute_error(val_y, val_predictions)
    
    return mae

# Compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    # Create a new model with the current max_leaf_nodes value
    laptop_model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
    
    # Calculate MAE using the get_mae function
    my_mae = get_mae(laptop_model, train_X, train_y, val_X, val_y)
    
    # Print the results
    print("Max leaf nodes: %d \t Mean Absolute Error: %.2f" % (max_leaf_nodes, my_mae))
