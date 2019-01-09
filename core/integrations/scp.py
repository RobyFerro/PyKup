import paramiko
from paramiko import SSHClient
from scp import SCPClient

from modules import env


class SCPUpload:
	
	def __init__(self, config_file):
		self.config = env.get_config(config_file)['SCP_CONFIGURATION']
		
		self.ssh = SSHClient()
		self.ssh.load_system_host_keys()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.connect(
			self.config["SCP_HOSTNAME"],
			self.config["SCP_PORT"],
			self.config["SCP_USERNAME"],
			self.config["SCP_PASSWORD"]
		)
	
	def upload(self, file, remote_folder):
		scp = SCPClient(self.ssh.get_transport())
		scp.put(f'{file}', recursive=True, remote_path=remote_folder)
		scp.close()
	
	def close_scp_connection(self):
		self.ssh.close()
	
	def check_backup_age(self, remote_folder):
		sftp = self.ssh.open_sftp()
		sftp.chdir(path=remote_folder)

# TODO: Complete backup age
