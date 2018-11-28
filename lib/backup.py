import tarfile
import time
import getpass
import datetime
from model import log


class Backup:
	
	def __init__(self, dir):
		self.directory = dir
	
	def run(self):
		date = time.time()
		
		filename = f'backup-{date}.tar.gz'
		
		try:
			tar = tarfile.open(filename, 'w:gz')
			tar.add(self.directory, filename)
			tar.close()
			
			insert = log.Log().create(
				type='INFO',
				description=f'Created .tar file of {self.directory} directory',
				user=getpass.getuser(),
				created_at=datetime.datetime.now()
			)
			
			insert.save()
		
		except Exception as msg:
			print(msg)
			return False
		return True
