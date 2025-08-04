import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
df = pd.read_csv("flood_dataset.csv")

# Features and target
X = df.drop("flood", axis=1)
y = df["flood"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model to file
with open("flood_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as flood_model.pkl")
