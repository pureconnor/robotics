import os
import time
import subprocess
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET','POST'])
async def incoming_sms():
    print('Message Received')
    body = request.values.get('Body', None)
    number = request.values.get('From', None)
    resp = MessagingResponse()

    print('Message body: ', body)
    if(body is not None):
        rawBody = "".join(body.split()).lower()
        print('Stripped message: ', rawBody)

    if rawBody == 'intelligentavoidance':
        resp.message('Got it. I will run intelligent object avoider for 15 seconds')
    elif rawBody == "findmeacoke": 
        resp.message("Got it. I will try to find a coke in 15 seconds")
    elif rawBody == "spin":
        resp.message("Got it. I will go do a sick spin for 15 seconds")
    else:
        resp.message("Sorry, i'm not sure what you are looking for")

    return str(resp)

def startAvoidance():
    cmd = 'python3 /home/pi/RoboticsFall2019GSU/Module5/Exercise\ 1/robot.py'
    proc = subprocess.Popen("exec " + cmd, stdout=subprocess.PIPE, shell=True)
    time.sleep(15)
    proc.kill()

if __name__ == "__main__":
    app.run(debug=False)

