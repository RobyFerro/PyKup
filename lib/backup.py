import tarfile
import time
import getpass
import datetime
import json
import subprocess
from model import log
import os


class Backup:

	def __init__(self, dir):
		self.directory = dir

	def run(self):
		date = time.time()

		filename = f'backup-{date}.tar.gz'

		try:
			tar = tarfile.open(filename, 'w:gz')
			tar.add(self.directory, filename)
			tar.close()

			insert = log.Log().create(
				type='INFO',
				description=f'Created .tar file of {self.directory} directory',
				user=getpass.getuser(),
				created_at=datetime.datetime.now()
			)

			insert.save()

		except Exception as msg:
			print(msg)
			return False
		return True

	@staticmethod
	def dump():

		with open('config/database.json') as f:
			db_config = json.load(f)

		if db_config['db_connection'] == 'pgsql':

			os.putenv('PGPASSWORD', db_config['db_password'])

			c = subprocess.Popen([
				f'pg_dump',
				f'--host={db_config["db_host"]}',
				f'--user={db_config["db_username"]}',
				f'--dbname={db_config["db_name"]}',
				f'--file=./test.dump'
			], stdout=subprocess.PIPE)

			return c.communicate()[0]

		elif db_config['db_connection'] == 'mysql':
			print('To be completed')

		return True
