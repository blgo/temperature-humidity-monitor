#!/usr/bin/python
import sys
import datetime

import Adafruit_DHT

import json
import requests

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 4 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
    #Where the data will be sent: POST API URL
    endpoint = sys.argv[3]

else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin# http://URL/POST')
    print('example: sudo ./Adafruit_DHT.py 2302 4 http://httpbin.org/post - Read from an AM2302 connected to GPIO #4 and post sensors data to API endpoint')
    sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    # print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    # Read sensor values. Prepare our sensor data in JSON format.
    payload = json.dumps({
        "temperature": round(temperature, 1),
        "humidity": round(humidity, 1)
    })

    #Test endpoint
    payload = { "date" : datetime.datetime.now().isoformat(), "room" : "bedroom", "temperature" : temperature, "humidity" : humidity }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    #print("Sending sensor data to API endpoint: ", payload)

    response = requests.post(endpoint, data=json.dumps(payload), headers=headers)
    #print(response.text)
    #print(response.status_code, response.reason) #HTTP


else:
    print('Failed to get reading. Try again!')
    sys.exit(1)

