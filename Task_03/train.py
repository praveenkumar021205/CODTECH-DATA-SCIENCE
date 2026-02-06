import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load data
df = pd.read_csv('data.csv')

# Train model
model = LinearRegression()
model.fit(df[['sqft', 'bedrooms']], df['price'])

# Save the "brain" of the project
joblib.dump(model, 'model.pkl')
print("Model created and saved as model.pkl!")
