from peewee import *
import datetime


db = SqliteDatabase('./database.db')


class Log(Model):
	type = CharField()
	description = TextField()
	
	class Meta:
		database = db
