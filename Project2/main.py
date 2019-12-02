import sys
import os
import json
import subprocess, signal
import FaceDetector
import SMSServer
import creds
import threading
import time
from twilio.rest import Client

account_sid = creds.account_sid
auth_token = creds.auth_token
client = Client(account_sid, auth_token)
phoneNumbers = creds.phoneNumbers

def startSMSSever():
    print('='*50, '\nSetting up SMS Server. Please wait....\n')
    os.system('python3 SMSServer.py')
    
def exposeServer():
    print('='*50, '\nExposing SMS Server via burrow.io. Please wait....\n')
    os.system('curl -Ls https://burrow.io/BNNfnYYM-P44mHceY | bash -s >/dev/null')
    
def sendMessage(identity):
    message = client.messages.\
                create(
                    body= 'Hi, {}!\
                        \nWhat would you like me do?\
                        \nIntelligent avoidance\
                        \nFind you a coke\
                        \nDo a spin'.format(identity),
                    from_= '+12568297127',
                    to= str(phoneNumbers[identity])
                )
    print('Message Sent! Send ID: ', message.sid)

if __name__ == "__main__":
    os.system('sudo modprobe bcm2835-v4l2 >/dev/null 2>&1')

    t1 = threading.Thread(target=startSMSSever)
    t2 = threading.Thread(target=exposeServer)

    t1.start()
    time.sleep(5)
    t2.start()
    time.sleep(5)
    
    
    print('='*50, '\nDetecting face. Hold still....')
    identity = FaceDetector.getFace()

    if identity != 'Unknown' and identity != 0:
        print('\nPerson detected!\nHi', identity, '!')
        if identity in phoneNumbers:
            sendMessage(identity)
        else:
            sys.exit('No phone number stored for: ', identity)
    else:
        print('Sorry, I wasn\t able to detect anybody I know')
        sys.exit("No face detected")
    




    