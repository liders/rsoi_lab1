import requests
import authorization
import json


class AccountInfo:
	#access_token = None
	url = 'https://money.yandex.ru/'

	def get_header(self, token):
		self.header = {'Authorization': 'Bearer ' + token,
						'Content-Type': 'application/x-www-form-urlencoded',
						'Content-Length': 0}
		return self.header

	def receive_account_info(self, access_token):
		self.main_url = self.url + 'api/account-info'
	   	self.headers = self.get_header(token=access_token)
		self.r = requests.post(self.main_url, headers=self.headers)
		
		return json.loads(self.r.text)

	def receive_operation_history(self, access_token):
		self.main_url = self.url + 'api/operation-history'

	   	self.params = {'record': 99}
	   	self.headers = self.get_header(token=access_token)	

		self.r = requests.post(self.main_url, headers=self.headers, params=self.params)
		return json.loads(self.r.text)