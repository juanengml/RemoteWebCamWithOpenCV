#not work with me
import rtsp
client = rtsp.Client(rtsp_server_uri = 'rtsp://admin@192.168.0.34')
client.read().show()
client.close()