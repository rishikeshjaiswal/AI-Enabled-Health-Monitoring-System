import unittest
from health_monitoring.monitor import HealthMonitor

class TestSystemIntegration(unittest.TestCase):
    def setUp(self):
        self.monitor = HealthMonitor()

    def test_end_to_end(self):
        """Simulate system integration test"""
        data_stream = [
            [75, 122, 98.7],
            [110, 150, 101.2],
            [65, 115, 97.5]
        ]
        results = [self.monitor.predict_health(d)[0] for d in data_stream]
        self.assertEqual(len(results), 3)  # 3 predictions 
