import unittest
from health_monitoring.monitor import HealthMonitor

class TestModelInputs(unittest.TestCase):
    def setUp(self):
        self.monitor = HealthMonitor()

    def test_invalid_input(self):
        """Model should raise error for wrong input shape"""
        with self.assertRaises(Exception):
            self.monitor.predict_health([999])  # invalid input 
