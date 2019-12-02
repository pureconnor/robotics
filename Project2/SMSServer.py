from flask import Flask
from flask import request
from flask import redirect
from flask_ngrok import run_with_ngrok
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)
# run_with_ngrok(app)

@app.route("/sms", methods=['GET','POST'])
def incoming_sms():
    body = request.values.get('Body', None)
    number = request.values.get('From', None)
    resp = MessagingResponse()

    print('Message body: ', body)
    if(body is not None):
        body = body.lower() 

    if body == 'coke':
        resp.message('Got it. I will go find the coke')
    elif body == 'candy': 
        resp.message('Got it. I will go find the candy')
    elif body == 'phone charger':
        resp.message('Got it. I will go find the phone charger')
    else:
        resp.message('Sorry, i\'m not sure what you are looking for')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=False)

