import os
import time
import sys
import paho.mqtt.client as mqtt
import json

THINGSBOARD_HOST = 'delrey.td.utfpr.edu.br'
ACCESS_TOKEN = 'cd0X5wbXhMbHeJrcACSc'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=0.1

sensor_data = {'FACES': 0, 'SENSOR_PRESENCA': 0}

next_reading = time.time()
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

def GET_DATA():
   try:
    data = open("data.txt").read().split()
    if not data:
         return [0,0]
    else:
         return data
   except:
   	return [0,0]


try:
    while True:
        faces,presenca = GET_DATA()
        print(u"faces: %s, SENSOR_PRESENCA: %s" % (faces, presenca))
        sensor_data['FACES'] = faces
        sensor_data['SENSOR_PRESENCA'] = presenca

        # Sending humidity and temperature data to ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
