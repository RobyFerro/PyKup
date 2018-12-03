import onedrivesdk
import json

class OneDrive:
	
	def __init__(self):
		with open('../../config/integrations/onedrive.json') as f:
			db_config = json.load(f)
		
		self.redirect_uri = db_config["redirect_uri"]
		self.client_secret = db_config["client_secret"]
		self.client_id = db_config["client_id"],
		self.api_base_url = db_config["api_base_url"]
		self.scopes = db_config["scopes"]
		
	
	def connect(self):
		http_provider = onedrivesdk.HttpProvider()
		auth_provider = onedrivesdk.AuthProvider(
			http_provider=http_provider,
			client_id=str(self.client_id),
			scopes=self.scopes)
		
		client = onedrivesdk.OneDriveClient(self.api_base_url, auth_provider, http_provider)
		auth_url = client.auth_provider.get_auth_url(self.redirect_uri)
		
		# Ask for the code
		print('Paste this URL into your browser, approve the app\'s access.')
		print('Copy everything in the address bar after "code=", and paste it below.')
		print(auth_url)
		code = input('Paste code here: ')
		
		return client.auth_provider.authenticate(code, self.redirect_uri, self.client_secret)
