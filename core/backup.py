import datetime
import getpass
import os
import subprocess
import tarfile
import time

from core.integrations import dropbox, scp, telegram
from model import log
from modules import env


class Backup:
	dump = False
	file = False

	def __init__(self, directory, app_name, config, tg):
		self.directory = directory
		self.dump = None
		self.app_name = app_name
		self.config_file = config
		self.telegram = tg

	def database(self):
		date = time.time()

		db_config = env.get_config(self.config_file)["DATABASE_CONFIGURATION"]

		filename = f'{db_config["DB_NAME"]}-{date}.dump'

		if db_config['DB_CONNECTION'] == 'pgsql':

			os.putenv('PGPASSWORD', db_config['DB_PASSWORD'])

			c = subprocess.Popen([
				f'pg_dump',
				f'--host={db_config["DB_HOST"]}',
				f'--user={db_config["DB_USERNAME"]}',
				f'{db_config["DB_NAME"]}',
				f'--file=./exports/{filename}'
			], stdout=subprocess.PIPE)

			self.dump = f'exports/{filename}'

			return c.communicate()[0]

		elif db_config['DB_CONNECTION'] == 'mysql':

			os.putenv('PGPASSWORD', db_config['DB_PASSWORD'])

			with open(f'./exports/{filename}', 'w') as out:
				c = subprocess.Popen([
					f'mysqldump',
					f'--host={db_config["DB_HOST"]}',
					f'--user={db_config["DB_USERNAME"]}',
					f'--password={db_config["DB_PASSWORD"]}',
					f'{db_config["DB_NAME"]}'
				], stdout=out)

			self.dump = f'exports/{filename}'

			return c.communicate()[0]

		return True

	def content(self):

		date = time.time()

		filename = f'exports/backup-{self.app_name}-{date}.tar.gz'

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

		self.file = filename
		return True

	def upload(self, type, remote_folder):

		tg = telegram.TelegramBot(self.config_file)

		if type not in ['dropbox', 'scp']:
			print('Please select a correct upload driver')
			exit(255)

		if type == 'dropbox':
			if self.file is not None:
				dbx = dropbox.DropboxIntegration(f'{self.app_name}', self.config_file)
				dbx.upload(self.file)
				dbx.close_connection()

				if self.telegram is True:
					tg.send_confirm_message(
						f'Congratulations! Your {self.app_name} is correctly backuped in your dropbox account')

		elif type == 'scp':
			if self.file is not None:
				upload = scp.SCPUpload(self.config_file)
				upload.upload(f'{self.file}', remote_folder)
				upload.close_scp_connection()

				if self.telegram is True:
					tg.send_confirm_message(
						f'Congratulations! Your {self.app_name} is correctly backuped in your server')

	def delete_local_backup(self):
		os.remove(self.file)
		os.remove(self.dump)
