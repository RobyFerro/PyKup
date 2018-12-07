import os
import sys
from crontab import CronTab
from modules import env


class CronIntegration:
	
	def __init__(self, args):
		self.cron = CronTab(user=True)
		self.command = f'cd {os.getcwd()} && {sys.executable} {os.getcwd()}/pykup.py '
		self.app_name = args.app_name
		
		self.config = env.get_config(args.config_file)["CRONTAB_CONFIGURATION"]
		
		for opt in vars(args):
			if opt == 'directory' and args.directory is not None:
				self.command += f'-d {args.directory} '
			elif opt == 'app_name' and args.app_name is not None:
				self.command += f'-n {args.app_name} '
			elif opt == 'upload_driver' and args.upload_driver is not None:
				self.command += f'-uD {args.upload_driver} '
			elif opt == 'config_file' and args.config_file is not None:
				self.command += f'-cF {args.config_file} '
			elif opt == 'remote_folder' and args.remote_folder is not None:
				self.command += f'-rF {args.remote_folder} '
			elif opt == 'telegram' and args.telegram is not False:
				self.command += f'--telegram'
	
	def insert_new_job(self):
		
		job = self.cron.new(command=self.command, comment=f'{self.app_name}')
		job.hour.on(self.config["HOURS"])
		job.minutes.on(self.config["MINUTES"])
		job.enable()
		self.cron.write()
