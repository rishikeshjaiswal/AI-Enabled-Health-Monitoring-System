import pickle 
import numpy as np

class HealthMonitor:
    def __init__(self, model_path="models/health_model.pkl"):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict_health(self, data):
        """
        Predicts health status from input data.
        data: numpy array [heart_rate, blood_pressure, temperature]
        """
        arr = np.array([data])
        return self.model.predict(arr)
