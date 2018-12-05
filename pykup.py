#!/usr/bin/env python
import argparse
from modules import backup, cron
from sys import platform

if platform not in ['linux', 'linux2']:
	print("Incorrect operative system")
	exit(255)

parser = argparse.ArgumentParser(description='PyBack WebApp backup utils')

parser.add_argument('-d',action='store',dest='directory',help="Set a backup directory",type=str,default=None, required=True)
parser.add_argument('-n',action='store',dest='app_name',help="Define application name",type=str,default=None)
parser.add_argument('-cF',action='store',dest='config_file',help="Define configuration file",type=str,default=None, required=True)
parser.add_argument('-uD',action='store',dest='upload_driver',help="Define upload driver dropbox|scp",type=str,default=None)
parser.add_argument('-rF',action='store',dest='remote_folder',help="Define scp remote folder",type=str,default=None)
parser.add_argument('--cron',action='store_true',dest='cron',help="Set command in crontab",default=False)

args = parser.parse_args()

if args.cron is True:
	cron_tab = cron.CronIntegration(args)
	cron_tab.insert_new_job()

if args.directory is None:
	print('You must insert a directory')
	exit(255)

backup = backup.Backup(args.directory, args.app_name, args.config_file)

dump = backup.database()
file = backup.content()

backup.upload(args.upload_driver, args.remote_folder)
backup.delete_local_backup()
