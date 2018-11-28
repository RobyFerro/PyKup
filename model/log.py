from peewee import *
import datetime


db = SqliteDatabase('./database.db')


class Log(Model):
	type = CharField()
	description = TextField()
	user = CharField()
	created_at = TimestampField()
	
	class Meta:
		database = db
