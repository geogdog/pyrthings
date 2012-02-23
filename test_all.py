import unittest
from pyrthings import random_mac, random_asset_tag, random_ports

class TestSequenceFunctions(unittest.TestCase):
    def test_random_mac(self):
        self.assertEqual(len(random_mac()), 17)

    def test_random_asset_tag(self):
        self.assertEqual(len(random_asset_tag()), 6)

    def test_random_ports(self):
        self.assertTrue(isinstance(random_ports(), list))
