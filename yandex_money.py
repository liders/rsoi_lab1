from flask import Flask, redirect, request, render_template, url_for
import requests
import webbrowser
import urllib
import authorization
import account_information
import payment
import json


app = Flask(__name__)

oauth = authorization.OAuth()
inform = account_information.AccountInfo()
payment = payment.Payment()

@app.route('/')
def layout():	
	
	code = request.args.get('code')
	if code:
		print(code)
		oauth.receive_access_token(code=code)	
		access_token = oauth.get_access_token()
		return redirect(oauth.redirect_uri)
	return render_template('layout.html')

@app.route('/oauth', methods=['POST'])
def request_authorization():
	
	oauth.request_authorization()
	
	return redirect(url_for('layout'))



@app.route('/info', methods=['POST'])
def info():
	account_info_json = inform.receive_account_info(access_token=oauth.access_token)

	return render_template('account_information.html', account_info=json.dumps(account_info_json, indent=4).decode('unicode-escape'))


@app.route('/history', methods=['POST'])
def history():
	operation_history_json = inform.receive_operation_history(access_token=oauth.access_token)
	return render_template('account_history.html', operation_history=json.dumps(operation_history_json, indent=4).decode('unicode-escape'))

@app.route('/payment', methods=['POST'])
def payment_to_tel():
	payment_info_json = payment.request_payment(access_token=oauth.access_token)
	return json.dumps(payment_info_json, indent=4)

if __name__ == '__main__':
    app.run(debug=True)

