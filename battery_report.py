# -*- coding: utf-8 -*-
# This pyhton code is to read WINDOWS battery kevel and send it to UBIDOTS IOT PLATFORM



import paho.mqtt.client as mqtt #Python library to publish a message to the topic on the mqtt broker
import json #To convert Python string into json format
import time
import psutil #Library for system monitoring
from converter import JSON_to_UL #for conversion from JSON to ultralight

#Variable configuration of MQTT Broker
mqtt_broker_address = "127.0.0.1"
mqtt_broker_port = 1883
mqtt_keepalive = 60
username = "BBFF-NSSvtWReGIXTocFsjWHcHGDlqsPAsE"
password = ""
topic = "TempHumd005/attrs"
api_key = "/5jggokgpepnvsb2uv4s40d59ov"


class surface:
    '''A class to send the Battery Level'''

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
            #client.username_pw_set(username,password)
            client.connect(mqtt_broker_address,mqtt_broker_port,mqtt_keepalive)
            topic_battery = "{}/{}".format(api_key,topic)
            print(topic_battery)
            batteryObj = {}
            batteryObj['t'] = battery_value
            jsonFormat_battery = json.dumps(batteryObj)
            ultralight_format = JSON_to_UL(jsonFormat_battery)
            print "\nAfter conversion, ultralight battery: ",ultralight_format
            #print(jsonFormat_battery)
            client.publish(topic_battery,ultralight_format)
            time.sleep(30)
    except KeyboardInterrupt:
        print('\n It is cancelled')
