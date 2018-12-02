#!/usr/bin/env python
import argparse
from lib import backup
from sys import platform

if platform not in ['linux','linux2']:
	print("Incorrect operative system")
	exit(255)

parser = argparse.ArgumentParser(description='PyBack WebApp backup utils')
parser.add_argument('-d', action='store', dest='directory', help="Set a backup directory", type=str)

args = parser.parse_args()

if args.directory is None:
	print('You must insert a directory')
	exit(255)

backup = backup.Backup(args.directory)

dump = backup.database()
backup.file()
