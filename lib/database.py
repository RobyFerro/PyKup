import sqlite3


class Database:

    def __init__(self, database=None):

        if database is None:
            self.database = database
        else:
            self.database = './database.db'

    def connect(self):
        return sqlite3.connect(self.database)

