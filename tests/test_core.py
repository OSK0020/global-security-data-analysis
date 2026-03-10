import unittest
from src.core import process_security_data

class TestCore(unittest.TestCase):
    def test_processing(self):
        # Basic smoke test
        self.assertIsNotNone(process_security_data())
