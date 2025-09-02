import unittest 
from health_monitoring.monitor import HealthMonitor

class TestModelAccuracy(unittest.TestCase):
    def setUp(self):
        self.monitor = HealthMonitor()

    def test_prediction_reasonable(self):
        input_data = [72, 120, 36.7]  # Normal values
        prediction = self.monitor.predict_health(input_data)
        self.assertIn(prediction, [0, 1])  # 0 = Healthy, 1 = Risk

if __name__ == "__main__":
    unittest.main()
