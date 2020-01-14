# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/14 14:11
# @Author   : Fangyang
# @Software : PyCharm

import requests

# AppID = 18274882
API_Key = "bfHx8r1mG5HMimkDzSebjca2"
Secret_Key = "FDCLMUZR5CvAE3s7WEMeadMyD3myWgcr"


def get_access_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_Key}&client_secret={Secret_Key}"
    response = requests.get(host)
    if response:
        # print(response.json())
        result_json = response.json()
        return result_json["access_token"]

if __name__ == '__main__':
    pass
