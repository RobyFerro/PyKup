import unittest
from lib.integrations import dropbox

class TestOneDriveMethods(unittest.TestCase):
	
	def testConnection(self):
		dbx = dropbox.DropboxIntegration()
		dbx.upload()
		
