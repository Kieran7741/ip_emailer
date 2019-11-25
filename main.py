#!/usr/bin/env python3.7
import datetime
import time
from ip_reader import get_ip
from emailer import send_email

#CONFIGURE:
SLEEP_TIME = 120
SENDER = 'kieran7741@gmail.com'
RECIPIENTS = ['kieran7741@gmail.com']
PI_USERNAME = 'pi'
EMAIL_BODY = ''

print('Sleeping for {0}s to allow for internet connection to be established.'.format(SLEEP_TIME))
time.sleep(SLEEP_TIME)

with open('/tmp/ip.log', 'w') as f: 
    print('Fetched ip address at: ' + str(datetime.datetime.now()), file=f)
    ip = get_ip._get_ip()
    print(f'IP: {ip}', file=f) 
    send_email._send_email(SENDER, RECIPIENTS, {'text': 'ssh {0}@{1}'.format(PI_USERNAME, ip)}, subject='Raspberry pi IP address')
