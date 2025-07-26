import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle

# Load Dataset
df = pd.read_csv('heart.csv')

# Encode categorical (if any string columns)
from sklearn.preprocessing import LabelEncoder
categorical_cols = df.select_dtypes(include=['object']).columns
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Split Features & Target
X = df.drop('target', axis=1)
y = df['target']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Model
model = LogisticRegression()
model.fit(X_scaled, y)

# Save Model & Scaler
pickle.dump(model, open('heart_model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))
