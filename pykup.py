#!/usr/bin/env python
import sys, argparse
from lib import backup, logger

parser = argparse.ArgumentParser(description='PyBack WebApp backup utils')
parser.add_argument('-d', action='store', dest='directory', help="Set a backup directory", type=str)
parser.add_argument('-l', action='store_true', dest='log', help="Show log", )

args = parser.parse_args()

if args.log:
    log = logger.Logger()

if args.directory is None:
    print('You must insert a directory')
    exit(255)

backup = backup.Backup(args.directory)
backup.run()
