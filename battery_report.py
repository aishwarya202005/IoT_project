# -*- coding: utf-8 -*-
# This pyhton code is to read WINDOWS battery kevel and send it to UBIDOTS IOT PLATFORM



import paho.mqtt.client as mqtt #Python library to publish a message to the topic on the mqtt broker
import json #To convert Python string into json format
import time
import psutil #Library for system monitoring
#Variable configuration of MQTT Broker
mqtt_broker_address = ""
mqtt_broker_port = 1883
mqtt_keepalive = 60
username = ""
password = ""
topic = "/v1.6/devices"
device_label = "t-rh"

class surface:
    '''A class to send the Battery Level from Sahil Saini Surface Device'''

    def battery_level(self):
        '''A function to get the battery level'''
        battery = psutil.sensors_battery()
        percent = str(battery.percent)
        return percent


if __name__ == "__main__":
    try: 
        while True:
            system = surface()
            battery_value = system.battery_level()
            client = mqtt.Client()
            client.username_pw_set(username,password)
            client.connect(mqtt_broker_address,mqtt_broker_port,mqtt_keepalive)
            topic_battery = "{}/{}".format(topic,device_label)
            batteryObj = {}
            batteryObj['battery'] = battery_value
            jsonFormat_battery = json.dumps(batteryObj)
            client.publish(topic_battery,jsonFormat_battery)
            time.sleep(10)
    except KeyboardInterrupt:
        print('\n It is cancelled')
