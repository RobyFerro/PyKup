import unittest
from lib import onedrive

class TestOneDriveMethods(unittest.TestCase):
	
	def test_connection(self):
		connect = onedrive.OneDrive()
		connect.connect()
