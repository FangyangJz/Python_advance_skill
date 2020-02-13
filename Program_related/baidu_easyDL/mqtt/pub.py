# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2020/2/12 18:50
# @Author  : Fangyang
# @Software: PyCharm

import json
import base64
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code : {rc}")


def on_message(client, userdata, msg):
    print(f"{msg.topic}  {msg.payload}")


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("139.196.127.75", 1883, 600)

    with open("./image.jpg", 'rb') as f:
        content = str(base64.b64encode(f.read()), encoding='utf-8')
    print(type(content))

    a = {
        "name": "ddd.jpg",
        "content": content
    }
    json_str = json.dumps(a)
    client.subscribe("resp")
    client.publish("emqtt", payload=json_str, qos=0)
    client.loop_forever()
