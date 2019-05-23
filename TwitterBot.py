#!/usr/bin/env python
import os
from twython import Twython

# Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
CONSUMER_KEY = 'MY-CONSUMER-KEY'
CONSUMER_SECRET = 'MY-CONSUMER-SECRET'
ACCESS_KEY = 'MY-ACCESS-KEY'
ACCESS_SECRET = 'MY-ACCESS-SECRET'

# Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# Using our newly created object, utilize the update_status to send in the text passed in through CMD
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]
api.update_status(status='My current CPU temperature is '+temp+' C')

