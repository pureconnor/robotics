import sys
import os
import subprocess
import FaceDetector
import SMSServer
import threading
import time
from twilio.rest import Client

account_sid = 'ACc719adaaa0af09c174ab842b8c1fa55a'
auth_token = '4c54aa6cf9bb6f6b9ff9e8f044c782c5'
client = Client(account_sid, auth_token)
phoneNumbers = {'Connor': '+16783278571'}

def startSMSSever():
    print('='*50, '\nSetting up SMS Server. Please wait....\n')
    cmd = 'python3.5 SMSServer.py'
    os.system(cmd)
    
def exposeServer():
    os.system('cd /tmp && ./ngrok http 5000 >/dev/null 2>&1')
    # subprocess.call(['cd', '/tmp', '&&', './ngrok', 'http', '5000'], stdout=subprocess.PIPE)


def sendMessage(identity):
    message = client.messages.\
                create(
                    body= 'Hi, {}!\nWhat would you like me to bring you?\nCoke\nCandy\nPhone Charger'.format(identity),
                    from_= '+12568297127',
                    to= str(phoneNumbers[identity])
                )
    print('Message Sent! Send ID: ', message.sid)

if __name__ == "__main__":

    t1 = threading.Thread(target=startSMSSever)
    t2 = threading.Thread(target=exposeServer)
    
    t1.start()
    time.sleep(5)
    t2.start()

    
    print('='*50, '\nDetecting face. Hold still....')
    identity = FaceDetector.getFace()

    if identity != 'Unknown':
        print('\nPerson detected!\nHi', identity, '!')
        if identity in phoneNumbers:
            sendMessage(identity)
        else:
            sys.exit('No phone number stored for: ', identity)
    else:
        print('Sorry, I wasn\t able to detect anybody I know')
        sys.exit("No face detected")
    




    