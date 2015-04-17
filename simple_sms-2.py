
from flask import Flask, request
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)

numbers = list()

# texts to twilio phone number will receive a response from this endpoint
# the numbers are collected and kept in a list
@app.route("/sms", methods=['GET', 'POST'])
def collect():
    resp = twilio.twiml.Response()
    resp.message("Hello, Tally Pythonista!")

    number = request.values.get('From')
    if number not in numbers:
        numbers.append(number)

    return str(resp)

# this endpoint returns a list of the numbers that have texted your twilio number
@app.route("/numbers")
def collected_numbers():
    print '\n'
    return '\n'.join(numbers)


# this endpoint sends a message to all numbers in the list
@app.route("/send")
def send_to_all():
    # Find these values at https://twilio.com/user/account
    account_sid = 'your-twilio-account-sid'
    auth_token = "your-twilio-account-token"
    twilio_number = '+15555555555'
    client = TwilioRestClient(account_sid, auth_token)
    for number in numbers:
        client.messages.create(to=number, from_=twilio_number, body="Twilio is cool!")
    return ''


if __name__ == "__main__":
    app.run(debug=True)
