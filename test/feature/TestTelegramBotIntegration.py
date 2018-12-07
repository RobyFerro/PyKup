import unittest
from core.integrations import telegram

class TestOneDriveMethods(unittest.TestCase):
	
	tg = telegram.TelegramBot('../../config/config.ini')
	
	def testNewMessage(self):
		self.tg.send_confirm_message('Test message')
		
		
		
