from crontab import CronTab
import os
import sys
import json

class CronIntegration:
	
	def __init__(self, args):
		self.cron = CronTab(user=True)
		self.command = f'cd {os.getcwd()} && {sys.executable}{os.getcwd()} pykup.py '
		self.app_name = args.app_name
		
		with open('config/crontab/crontab.json') as f:
			self.config = json.load(f)
		
		for opt in vars(args):
			if opt == 'directory' and args.directory is not None:
				self.command += f'-d {args.directory} '
			elif opt == 'app_name' and args.app_name is not None:
				self.command += f'-n {args.app_name} '
			elif opt == 'database' and args.database is not None:
				self.command += f'-dB {args.database} '
			elif opt == 'upload_driver' and args.upload_driver is not None:
				self.command += f'-uD {args.upload_driver} '
			elif opt == 'scp_config' and args.scp_config is not None:
				self.command += f'-sC {args.scp_config} '
			elif opt == 'remote_folder' and args.remote_folder is not None:
				self.command += f'-rF {args.remote_folder} '
				
	def insert_new_job(self):
		
		job = self.cron.new(command=self.command, comment=f'{self.app_name}')
		job.hour.on(self.config["hours"])
		job.minutes.on(self.config["minutes"])
		job.enable()
		self.cron.write()
