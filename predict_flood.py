import pickle
import numpy as np

# Load model
with open("flood_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_flood(rainfall, temperature, humidity, water_level):
    input_data = np.array([[rainfall, temperature, humidity, water_level]])
    prediction = model.predict(input_data)[0]
    return "🌊 Flood likely!" if prediction == 1 else "✅ No flood expected."
