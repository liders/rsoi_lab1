from urllib import urlencode
from urllib import quote
import requests
import webbrowser
import urllib



class OAuth:
	client_secret = 'CC5342E7E97055FBA2815F7D30CED0010092C0C5DCBE1366C1CD4CFF48E63CD7A8A8CC577088ED47C22CD5184899748BE33BF32291AE415FE83AC547726B44E4'
	redirect_uri = 'http://127.0.0.1:5000'
	client_id = 'B5952149E3F49A084455C3A9F476112C5061B267B7F1713018D5AC853DB9E2AC'
	access_token = None

	def request_authorization(self):
		self.url = "https://money.yandex.ru/oauth/authorize"
		
		self.params = {'client_id': self.client_id, 
						'response_type': 'code', 
						'redirect_uri': self.redirect_uri,
						"scope": "operation-history payment-p2p account-info"}
			
		self.headers = {'Content-Type': 'application/x-www-form-urlencoded',
						'Content-Length': 0}
		print(urlencode(self.params).replace('+', '%20').replace('-', '%2D'))

		self.r = requests.post(self.url, headers=self.headers, 
								params=urlencode(self.params).replace('+', '%20').replace('-', '%2D'))
		
		webbrowser.open_new(self.r.url)

		


	def get_code_from_url(self):
		self.code = request.args.get('code')
		print('[INFO] in function get_code_from_url:' + self.code)
		return self.code


	def receive_access_token(self, code):
		
		print('[INFO] in function get_access_token')

		self.url = 'https://money.yandex.ru/oauth/token'
		self.headers = {'Content-Type': 'application/x-www-form-urlencoded',
						'Content-Length': 0}
		self.params = {'code': code,
						'client_id': self.client_id, 
						'grant_type': 'authorization_code', 
						'redirect_uri': self.redirect_uri,
						'client_secret': self.client_secret}

		self.r = requests.post(self.url, headers=self.headers, params=self.params)
		self.access_token_json = self.r.json()

		self.access_token = self.access_token_json["access_token"]
		print "ACCESS_TOKEN:" + self.access_token
		#webbrowser.open(self.redirect_uri, new=0, autoraise=True)

	def get_access_token(self):
		return self.access_token


