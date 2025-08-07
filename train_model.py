# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load dataset
df = pd.read_csv("app_cost_dataset.csv")

X = df.drop("cost", axis=1)
y = df["cost"]

# Preprocessing
categorical_cols = ['platform', 'complexity']
numeric_cols = ['auth', 'backend', 'payment', 'realtime', 'screens', 'duration']

preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(), categorical_cols)
], remainder='passthrough')

# Pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', XGBRegressor(n_estimators=100, random_state=42))
])

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"MAE: ${mae:.2f}")

# Save model
joblib.dump(model, "app_cost_model.pkl")
print("Model saved to app_cost_model.pkl")
