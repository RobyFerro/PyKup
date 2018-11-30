import tarfile
import time
import getpass
import datetime
import json
import subprocess
from model import log
from sys import platform


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
			
			if platform == "linux" or platform == "linux2":
				
				Popen([
					f'PGPASSWORD={db_config["db_password"]}',
					f'pg_dump',
					f'-h {db_config["db_host"]}',
					f'-U {db_config["db_username"]}',
					f'-d {db_config["db_name"]}',
					f'-f test.dump'
				])
			
			elif platform == 'win32':
				
				#
				# TODO Not working
				
				psql_env = dict(PGPASSWORD='wsgen')
				
				cmd = f'pg_dump -h 127.0.0.1 -p 5432 -U wsgen -d ulisse_svil1'
				
				with open('test.dump', 'wb') as f:
					popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True, env=psql_env)
					
					for stdout_line in iter(popen.stdout.readline, ""):
						f.write(stdout_line.encode('utf - 8'))
						
						popen.stdout.close()
						popen.wait()
		
		elif db_config['db_connection'] == 'mysql':
			print('To be completed')
		
		return True
