import paramiko
from paramiko import SSHClient
from scp import SCPClient
import json


class SCPUpload:
	
	def __init__(self, scp_config):
		with open(scp_config) as f:
			self.config = json.load(f)
			
			self.ssh = SSHClient()
			self.ssh.load_system_host_keys()
			self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.ssh.connect(
				self.config['hostname'],
				self.config["port"],
				self.config["username"],
			    self.config["password"]
			)

	def upload(self, file, remote_folder):
		scp = SCPClient(self.ssh.get_transport())
		scp.put(f'{file}', recursive=True, remote_path=remote_folder)
		scp.close()
		
	def __del__(self):
		self.ssh.close()
