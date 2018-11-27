import tarfile
import time
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
			
			insert = log.Log().create(type='INFO', description='Test')
			insert.save()
		
		except Exception as msg:
			print(msg)
			return False
		return True
