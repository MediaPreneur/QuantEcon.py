"""
Tests for ecdf.py

"""
import unittest
import numpy as np
from quantecon import ECDF


class TestECDF(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obs = np.random.rand(40)  # observations defining dist
        cls.ecdf = ECDF(cls.obs)

    def test_call_high(self):
        "ecdf: x above all obs give 1.0"
        # all of self.obs <= 1 so ecdf(1.1) should be 1
        self.assertAlmostEqual(self.ecdf(1.1), 1.0)

    def test_call_low(self):
        "ecdf: x below all obs give 0.0"
        # all of self.obs <= 1 so ecdf(1.1) should be 1
        self.assertAlmostEqual(self.ecdf(-0.1), 0.0)

    def test_ascending(self):
        "ecdf: larger values should return F(x) at least as big"
        x = np.random.rand()
        F_1 = self.ecdf(x)
        F_2 = self.ecdf(1.1 * x)
        self.assertGreaterEqual(F_2, F_1)

    def test_vectorized(self):
        "ecdf: testing vectorized __call__ method"
        t = np.linspace(-1, 1, 100)
        e = self.ecdf(t)
        self.assertEqual(t.shape, e.shape)
        self.assertEqual(e.dtype, float)
        t = np.linspace(-1, 1, 100).reshape(2, 2, 25)
        e = self.ecdf(t)
        self.assertEqual(t.shape, e.shape)
        self.assertEqual(e.dtype, float)
