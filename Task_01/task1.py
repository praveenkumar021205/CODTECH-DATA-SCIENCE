
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# 1. EXTRACT
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

# 2. TRANSFORM (The Pipeline)
# This automates filling missing values and scaling data
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')), 
    ('scaler', StandardScaler())
])

# Apply the pipeline
cleaned_data = pipeline.fit_transform(df)
df_final = pd.DataFrame(cleaned_data, columns=data.feature_names)

# 3. LOAD
df_final.to_csv('cleaned_data.csv', index=False)
print("Task 1 Complete: Cleaned data saved to 'cleaned_data.csv'")
