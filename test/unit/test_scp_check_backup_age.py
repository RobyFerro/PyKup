import unittest

from core.integrations import scp


class TestScpBackupAge(unittest.TestCase):
	
	def testFileAge(self):
		connector = scp.SCPUpload('../../config/config.ini')
		connector.check_backup_age('/home/webuser/test')
