
from flask import Flask
import twilio.twiml

app = Flask(__name__)

# texts to twilio phone number will receive a response from this endpoint
@app.route("/sms", methods=['GET', 'POST'])
def collect():
	resp = twilio.twiml.Response()
	resp.message("Hello, Tally Pythonista!")
	return str(resp)


if __name__ == "__main__":
		app.run(debug=True)
