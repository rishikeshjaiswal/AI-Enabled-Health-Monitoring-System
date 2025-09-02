# train_dummy_model.py
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
import os

# Dummy training data with 3 features (heart_rate, systolic_bp, diastolic_bp)
X = np.array([
    [60, 110, 70],
    [80, 130, 85],
    [90, 150, 95],
    [70, 120, 80]
])
y = np.array([0, 1, 1, 0])  # 0 = Healthy, 1 = Risk (dummy labels)

model = LogisticRegression()
model.fit(X, y)

os.makedirs("models", exist_ok=True)
with open("models/health_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Dummy 3-feature model trained and saved at models/health_model.pkl")
