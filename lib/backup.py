import tarfile
import time
from lib import logger


class Backup:

    def __init__(self, dir):
        self.directory = dir

    def run(self):
        date = time.time()
        log = logger.Logger()
        
        filename = f'backup-{date}.tar.gz'

        try:
            tar = tarfile.open(filename, 'w:gz')
            tar.add(self.directory, filename)
            tar.close()
            log.directory_backup()
            
        except Exception as msg:
            print(msg)
            return False
        return True
