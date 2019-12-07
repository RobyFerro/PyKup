import datetime
import os

import dropbox

from modules import env


class DropboxIntegration:
	dbx = None

	def __init__(self, destination, config_file):
		self.destination = destination
		self.config = env.get_config(config_file)['DROPBOX_INTEGRATION']
		self.dbx = dropbox.Dropbox(self.config['ACCESS_TOKEN'])

	def upload(self, file):
		f = open(file, 'rb')
		file_size = os.path.getsize(file)
		chunk_size = 4 * 1024 * 1024

		if file_size <= chunk_size:
			with open(file, 'rb') as f:
				self.dbx.files_upload(f.read(), f'/{self.destination}/{file}')
		else:
			upload_session_start_result = self.dbx.files_upload_session_start(f.read(chunk_size))
			cursor = dropbox.files.UploadSessionCursor(
				session_id=upload_session_start_result.session_id,
				offset=f.tell()
			)

			commit = dropbox.files.CommitInfo(path=f'/{self.destination}/{file}')

			while f.tell() < file_size:
				if (file_size - f.tell()) <= chunk_size:
					self.dbx.files_upload_session_finish(f.read(chunk_size), cursor, commit)
				else:
					self.dbx.files_upload_session_append(f.read(chunk_size), cursor.session_id, cursor.offset)
					cursor.offset = f.tell()

		self.check_backup_age()

	def check_backup_age(self):

		now = datetime.datetime.now()

		file_list = self.dbx.files_list_folder(path=f'/{self.destination}/exports')

		for file in file_list.entries:

			if abs(now - file.server_modified).days > int(self.config["DBX_MAX_BACKUP_AGE"]):
				self.dbx.files_delete_v2(path=file.path_lower)

	def close_connection(self):
		if self.dbx is not None:
			self.dbx._session.close()
