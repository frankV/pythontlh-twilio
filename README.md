PythonTLH Sample Twilio App
===========================

This repository contains the sample Twilio apps we demonstrated at PythonTLH's first meeting, April 17, 2015.

###Sign Up for Twilio
First thing you should do is sign up for Twilio. Use the code we sent in the newsletter or visit the MeetUp page.

After you sign up for Twilio and enter your code, you'll have an SID and Auth-Token. Next you'll want to assign a phone number to your account.

The phone number will have two URLs needed to interface with an application
  1. a URL to send SMS requests to
  2. a URL to send voice calls to

In the demo we used [ngrok](https://ngrok.com/) to tunnel our app to the URL we provided Twilio.

###Running the Sample Applications

Dependencies
  - `pip` is needed to install package dependencies
  - [`Flask`](http://flask.pocoo.org/) is used as our application framework
  - your machine will need a Python interpreter installed

With the dependencies satisfied, to install all packages, run:
```shell
user@host:/<path-to-repo>$ pip install -r requirements.txt
```

Afterwards, if all your Twilio settings are updated and you have a tunnel or URL pointing at your app, run this to start the flask application:
```shell
user@host:/<path-to-repo>$ python simple_sms.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
```

If you need any help, tweet at us: [@PythonTLH](https://twitter.com/PythonTLH) or email me.