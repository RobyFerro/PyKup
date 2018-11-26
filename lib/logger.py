import os
from lib import database


class Logger:

    def __init__(self):
        self.db = database.Database()
