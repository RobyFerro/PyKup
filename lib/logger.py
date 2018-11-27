import os
from lib import database


class Logger:
	
	def __init__(self):
		self.db = database.Database()
		
	def directory_backup(self):
		conn = self.db.connect()
		c = conn.cursor()
		
		c.execute("INSERT INTO log VALUES ('INFO','description','','')")
		conn.commit()
