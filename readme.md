![Pykup](logo.jpg) 
# PyKup - WebApp backup manage

A simple tool to easily manage and schedule backup for any web app!
With PyKup you can backup your web applications in just one command.
Everything will be compressed and stored in your favorite storage location.

## Usage

```
python pykup.py -d <APP_FOLDER> -cF <PATH_CONFIG_FILE> -uD <UPLOAD_DRIVER dropbox|scp> --cron 
```

## Multiple application backup
With crontab integration you can schedule multiple application backup:

```
python pykup.py -d <APP_FOLDER_1> -cF <PATH_CONFIG_FILE_1> -uD <UPLOAD_DRIVER dropbox|scp> --cron 
python pykup.py -d <APP_FOLDER_2> -cF <PATH_CONFIG_FILE_2> -uD <UPLOAD_DRIVER dropbox|scp> --cron 
```

## Getting started
First of all ensure that Python 3 is installed on your machine, then you can get all file with:

```
git clone https://github.com/RobyFerro/PyKup.git
```

Install all requirements with:

```
pip install -r requirements.txt
```

After that you can get all information by typing:
```
usage: pykup.py [-h] -d DIRECTORY [-n APP_NAME] -cF CONFIG_FILE
                [-uD UPLOAD_DRIVER] [-rF REMOTE_FOLDER] [--cron]

PyBack WebApp backup utils

optional arguments:
  -h, --help         show this help message and exit
  -d DIRECTORY       Set a backup directory
  -n APP_NAME        Define application name
  -cF CONFIG_FILE    Define configuration file
  -uD UPLOAD_DRIVER  Define upload driver dropbox|scp
  -rF REMOTE_FOLDER  Define scp remote folder
  --cron             Set command in crontab
  --telegram         Send telegram notification after backup
```

## Config
To config your web app you should rename config.ini.example in config directory
and replace all values with your parameters.

You can set multiple .ini file to schedule multiple backup

```
first-app.ini
second-app.ini
third-app.ini
```

**This trick it will be useful combinated with --cron option.**

## Crontab events
To set the current command inside linux crontab job you've just to specify --cron option.
Use the following command to show all existing crontab job:
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

## Telegram confirm notification

To send notification to your own telegram channel you've to create a [Telegram bot](https://core.telegram.org/bots#6-botfather)

* Insert your TOKEN and channel name in config.ini file

### Todo list:
- [x] File backup and compression
- [x] Log activity
- [x] PostgreSQL dump
- [x] MySQL dump
- [x] Dropbox integration
- [x] SCP Sync
- [x] Rsync integration
- [x] Crontab integration
- [x] Telegram confirm notification
- [ ] Telegram bot remote control
- [ ] Google Drive Integration
