import tarfile
import time
import getpass
import datetime
import json
import subprocess
from model import log
import os


class Backup:
	dump = False
	
	def __init__(self, dir):
		self.directory = dir
		self.dump = None
	
	def file(self):
		
		date = time.time()
		
		filename = f'backup-{date}.tar.gz'
		
		try:
			tar = tarfile.open(filename, 'w:gz')
			tar.add(self.directory)
			
			if self.dump is not None:
				tar.add(self.dump)
			
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
	
	def database(self):
		date = time.time()
		
		with open('config/database.json') as f:
			db_config = json.load(f)
		
		filename = f'{db_config["db_name"]}-{date}.dump'
		
		if db_config['db_connection'] == 'pgsql':
			
			os.putenv('PGPASSWORD', db_config['db_password'])
			
			c = subprocess.Popen([
				f'pg_dump',
				f'--host={db_config["db_host"]}',
				f'--user={db_config["db_username"]}',
				f'--dbname={db_config["db_name"]}',
				f'--file=./tmp/{filename}'
			], stdout=subprocess.PIPE)
			
			self.dump = f'tmp/{filename}'
			
			return c.communicate()[0]
		
		elif db_config['db_connection'] == 'mysql':
			
			os.putenv('PGPASSWORD', db_config['db_password'])
			
			with open(f'./tmp/{filename}', 'w') as out:
				c = subprocess.Popen([
					f'mysqldump',
					f'--host={db_config["db_host"]}',
					f'--user={db_config["db_username"]}',
					f'--password={db_config["db_password"]}',
					f'{db_config["db_name"]}'
				], stdout=out)
			
			self.dump = f'tmp/{filename}'
			
			return c.communicate()[0]
		
		return True
