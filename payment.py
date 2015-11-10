import requests
from urllib import urlencode


class Payment:
	url = 'https://money.yandex.ru/'
	#access_token = None

	def get_header(self, token):
		self.header = {'Authorization': 'Bearer ' + token,
						'Content-Type': 'application/x-www-form-urlencoded',
						'Content-Length': 0}
		return self.header

	def request_payment(self, access_token):
		self.main_url = self.url + 'api/request-payment'
		self.headers = self.get_header(token=access_token)

		
		self.params = {	'to': '410013672930559',
						#'test_payment': 'true',
						'amount': '10.00',
						"pattern_id": "p2p"}
		"""
		self.params = {'pattern_id': 'phone-topup',
						
						'phone-number': '',
						'amount': '10.00'}
		"""
		print(urlencode(self.params).replace('+', '%20').replace('-', '%2D'))
		self.r = requests.post(self.main_url, headers=self.headers, params=urlencode(self.params).replace('+', '%20').replace('-', '%2D'))

		return self.r.json()

