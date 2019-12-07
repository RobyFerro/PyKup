import sqlite3


class Database:
	connection = None

	def __init__(self, database=None):

		if database is not None:
			self.database = database
		else:
			self.database = './database.db'

	def connect(self):
		self.connection = sqlite3.connect(self.database)
		return self.connection

	def close_connection(self):
		self.connection.close()
