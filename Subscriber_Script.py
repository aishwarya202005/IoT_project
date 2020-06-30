
import paho.mqtt.client as mqtt
mqtt_broker_address = "localhost"
mqtt_broker_port = 1883
mqtt_keepalive = 60
username="username"
password="password"
def on_connect(client, userdata, flags, rc):
	print('Connection Result Status: {}'.format(mqtt.connack_string(rc)))
	#Subscribing if we lose connection and reconnect then subscriptions will
	#be renewed
	client.subscribe("temp/myroom")

def on_subscribe(client, userdata, mid, granted_qos):
	print('Subscribed Qos: {}'.format(granted_qos[0]))

def on_message(client, userdata, message):
	print(' Topic Name : {} and Received Message: {}'.format(message.topic,str(message.payload)))
    
if __name__ == "__main__":
	print('Python code to establish a connection and subscribe to a topic \
and print the received messages')
	client = mqtt.Client()
	client.username_pw_set(username,password)
	client.on_connect = on_connect
	client.on_subscribe = on_subscribe
	client.on_message = on_message
	client.connect(mqtt_broker_address,mqtt_broker_port,mqtt_keepalive)
	client.loop_forever()
