#!/usr/bin/env python3
import unittest
from resilient_kingdom.core import *

class SmokeTests(unittest.TestCase):
    def test_scenarios(self):
        rows=run_scenarios(6)
        self.assertEqual(len(rows), 6)
        self.assertTrue(all('energy' in r for r in rows))
    def test_rejects_negative(self):
        with self.assertRaises(ValueError):
            run_scenarios(-1)
        with self.assertRaises(ValueError):
            scenario(-1)
    def test_trace(self):
        t=Trace(); t.add(0, 1.0, 'x'); self.assertGreater(t.mean(), 0)
    def test_domain(self):
        self.assertEqual(PROJECT, 'resilient-kingdom')

if __name__ == '__main__': unittest.main()
