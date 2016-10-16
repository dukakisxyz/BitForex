# BitFOREX – Providing current and historical foreign exchange rates as published by the European Central Bank, in exchange for bitcoin.
# The rates are updated daily around 4PM CET
# Rates are quoted against the Euro by default. Quote against a different currency by setting the base parameter in your request.

import requests
import json
import yaml

from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Initiating Flask, Wallet and Payment
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

#Adding the 402 – Payment required
@app.route("/latest")
@app.route("/latest/<string:base>")
@payment.required(3000)
def fetch_latest_data(base=None):
	
	if base == None:
		base_url = ""
	else:
		base_url = "?base="+base

	try:
		data = requests.get("http://api.fixer.io/latest"+base_url)
		return (data.text)
	except:
		exception = {"Exception raised" : "There was an error fetching your data"}
		return json.dumps(exception)

@app.route("/get/<string:date>")
@app.route("/get/<string:date>/<string:base>")
@payment.required(3000)
def fetch_historical_data(date=None, base = None):
	
	date = date
	if base == None:
		base_url = ""
	else:
		base_url = "?base="+base
		
	try:
		data = requests.get("http://api.fixer.io/"+date+base_url)
		return (data.text)
	except:
		exception = {"Exception raised" : "There was an error fetching your data"}
		return json.dumps(exception)

# Init Host
if __name__=='__main__':
	app.run(host='::', port='9000')