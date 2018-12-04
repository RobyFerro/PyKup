import dropbox
import json
import datetime


class DropboxIntegration:
	dbx = None
	
	def __init__(self, destination):
		self.destination = destination
		with open('config/integrations/dropbox.json') as f:
			self.config = json.load(f)
			self.dbx = dropbox.Dropbox(self.config["access_token"])
	
	def upload(self, file):
		
		self.check_backup_age()
		
		with open(file, 'rb') as f:
			self.dbx.files_upload(f.read(), f'/{self.destination}/{file}')
			
	def check_backup_age(self):
		
		now = datetime.datetime.now()
		
		file_list = self.dbx.files_list_folder(path=f'/{self.destination}/exports')
		
		for file in file_list.entries:
			
			if abs(now - file.server_modified).days > self.config["max_backup_age"]:
				self.dbx.files_delete_v2(path=file.path_lower)
		
	def __del__(self):
		if self.dbx is not None:
			self.dbx._session.close()
