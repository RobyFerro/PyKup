# PyKup - WebApp backup manager

A simple tool to easily backup your WebApp

## Getting started
First of all ensure that Python 3 is installed on your machine. 
Install all requirements with:

```
pip install -r requirements.txt
```

After that you can get all information by typing:
```
python pykup.py --help

usage: pykup.py [-h] [-d DIRECTORY] [-n APP_NAME] [-dB DATABASE]
                [-uD UPLOAD_DRIVER] [-sC SCP_CONFIG] [-rF REMOTE_FOLDER]
                [--cron]

PyBack WebApp backup utils

optional arguments:
  -h, --help         show this help message and exit
  -d DIRECTORY       Set a backup directory
  -n APP_NAME        Define application name
  -dB DATABASE       Define database configuration file
  -uD UPLOAD_DRIVER  Define upload driver dropbox|scp
  -sC SCP_CONFIG     Define scp connection configuration
  -rF REMOTE_FOLDER  Define scp remote folder
  --cron             Set command in crontab
```

## Config
To config your web app you should rename all .json.example in config directory
and replace all values with your parameters.


## Crontab events
With "--cron" option you can schedule your backup in crontab jobs.
You can show all cron jobs by typing:

```
crontab -l
```

## Dropbox integration

To upload your backups on dropbox you've to create a new application inside your [Dropbox account](https://www.dropbox.com/developers/apps/create) 
and follow this steps:

* Select Dropbox API
* Select "App folder"
* Select your app name

Once created you've to generate a new access token and put it on config/integrations/dropbox.json

### Todo list:
- [x] File backup and compression
- [x] Log activity
- [x] PostgreSQL dump
- [x] MySQL dump
- [x] Dropbox integration
- [x] SCP Sync
- [x] Crontab integration
- [ ] Google Drive Integration
- [ ] Mega integration
