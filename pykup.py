#!/usr/bin/env python
import argparse
from lib import backup
from sys import platform

if platform not in ['linux','linux2']:
	print("Incorrect operative system")
	exit(255)

parser = argparse.ArgumentParser(description='PyBack WebApp backup utils')
parser.add_argument('-d', action='store', dest='directory', help="Set a backup directory", type=str)
parser.add_argument('-n', action='store', dest='app_name', help="Define application name", type=str)
parser.add_argument('-dB', action='store', dest='database', help="Define database configuration file", type=str)

args = parser.parse_args()

if args.directory is None:
	print('You must insert a directory')
	exit(255)

backup = backup.Backup(args.directory, args.app_name, args.database)

dump = backup.database()
file = backup.file()
backup.upload()
