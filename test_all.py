import unittest
from pyrthings import random_mac, random_asset_tag, random_ports

class TestSequenceFunctions(unittest.TestCase):
    def test_random_mac(self):
        mac = random_mac()
        self.assertEqual(len(mac), 17)

    def test_random_asset_tag(self):
        asset_tag = random_asset_tag()
        self.assertEqual(len(asset_tag), 6)

    def test_random_ports(self):
        ports = random_ports()
        self.assertTrue(isinstance(ports, list))

    def test_random_ip_in_network(self):
        pass

    def test_random_ip_in_range(self):
        pass

if __name__ == '__main__':
    unittest.main()
