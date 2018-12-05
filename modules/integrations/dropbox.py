import dropbox
import datetime
from modules import env


class DropboxIntegration:
	dbx = None
	
	def __init__(self, destination, config_file):
		self.destination = destination
		self.config = env.get_config(config_file)['DROPBOX_INTEGRATION']
		self.dbx = dropbox.Dropbox(self.config['ACCESS_TOKEN'])
		
	
	def upload(self, file):
		
		self.check_backup_age()
		
		with open(file, 'rb') as f:
			self.dbx.files_upload(f.read(), f'/{self.destination}/{file}')
			
	def check_backup_age(self):
		
		now = datetime.datetime.now()
		
		file_list = self.dbx.files_list_folder(path=f'/{self.destination}/exports')
		
		for file in file_list.entries:
			
			if abs(now - file.server_modified).days > int(self.config["DBX_MAX_BACKUP_AGE"]):
				self.dbx.files_delete_v2(path=file.path_lower)
				
	def close_connection(self):
		if self.dbx is not None:
			self.dbx._session.close()
		
