#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Datetime :   2020/2/12 下午7:23
@Author   :   Fangyang
"""
import base64
import json
import os
from utils.log import LogModule
import time

import paho.mqtt.client as mqtt


class Sub:
    def __init__(self):
        self.pic_dir = './picture'
        self.pic_dir_size = 1000  # 文件夹只能存1000张图片

        self.log = LogModule(name='mqtt', level='info')
        self.recv_count = 0

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.hostname = "139.196.127.75"
        self.port = 1883
        self.client.connect(self.hostname, self.port, 600)
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        self.log.write_log("Connected with result code " + str(rc))
        client.subscribe('emqtt', qos=0)

    def on_message(self, client, userdata, msg):
        self.log.write_log(f"{msg.topic}, recv_count:{self.recv_count}")
        self.recv_count += 1
        cur_datetime_str = time.strftime("%Y%m%d_%H_%M_%S",time.localtime())

        #TODO
        # 1. 低电量报警
        # 2. 图片采集失败提示
        recv_dict = json.loads(msg.payload)
        if recv_dict['content']:

            # 保证文件夹内图片数量一定
            pic_list = os.listdir(self.pic_dir)
            if len(pic_list) > self.pic_dir_size:
                os.remove(f"{self.pic_dir}/{pic_list[0]}")

            try:
                # file_name_str = recv_dict['name']
                file_name_str_list = recv_dict['name'].split('.')
                file_name_str = f"{file_name_str_list[0]}_{cur_datetime_str}.{file_name_str_list[1]}"
                
                with open(f"{self.pic_dir}/{file_name_str}", "wb") as f:
                    xx = recv_dict['content'].encode("utf-8")
                    f.write(base64.b64decode(xx))
                self.client.publish("resp", f"Got it! Current pictures list:{pic_list}")
            except:
                self.client.publish("resp", f"write {file_name_str} meet problem!")
        else:
            self.client.publish("resp", f"content is empty !")


if __name__ == "__main__":
    s = Sub()
