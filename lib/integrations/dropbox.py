import dropbox
import json


class DropboxIntegration:
	dbx = None
	
	def __init__(self):
		with open('config/integrations/dropbox.json') as f:
			self.config = json.load(f)
			self.dbx = dropbox.Dropbox(self.config["access_token"])
	
	def upload(self, file):
		with open(file, 'rb') as f:
			self.dbx.files_upload(f.read(), f'/{file}')
	
	def __del__(self):
		if self.dbx is not None:
			self.dbx._session.close()
