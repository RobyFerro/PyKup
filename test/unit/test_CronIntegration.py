import unittest

from lib import cron


class TestCronIntegration(unittest.TestCase):

	def testCron(self):
		c = cron.CronIntegration()
		c.insert_new_job()
