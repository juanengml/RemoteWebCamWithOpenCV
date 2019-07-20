import os
import time
import sys
import paho.mqtt.client as mqtt
import json

THINGSBOARD_HOST = 'delrey.td.utfpr.edu.br'
ACCESS_TOKEN = 'cd0X5wbXhMbHeJrcACSc'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=0.2

sensor_data = {'FACES': 0,'BODY': 0, 'SENSOR_PRESENCA': 0}

next_reading = time.time() 

client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()


def get_data():
    FACES,BODY,SENSOR_PRESENCA = open("data.txt").read().split()
    return [FACES,BODY,SENSOR_PRESENCA]

try:
    while True:
        FACES,BODY,SENSOR_PRESENCA = get_data()
        print(u"FACES:%s BODY: %s, SENSOR_PRESENCA: %s" % (FACES,BODY, SENSOR_PRESENCA))
        sensor_data['FACES'] = FACES
        sensor_data['BODY'] = BODY
        sensor_data['SENSOR_PRESENCA'] = SENSOR_PRESENCA

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
