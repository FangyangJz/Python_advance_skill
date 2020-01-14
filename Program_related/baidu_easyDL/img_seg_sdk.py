# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/14 14:17
# @Author   : Fangyang
# @Software : PyCharm


# import urllib2
import requests
import base64
import json

import pycocotools.mask as mask_util
import cv2
import numpy as np

from get_access_token import get_access_token

'''
easydl图像分割
'''


def transform_img_to_req_data(img_path):
    with open(img_path, 'rb') as f:
        img_str = f.read()

    # img_str = base64.b64encode(img_str).decode("utf-8")
    img_str = str(base64.b64encode(img_str), "utf-8")
    params = {"image": img_str}
    encoded_data = json.dumps(params).encode('utf-8')
    return encoded_data


def send_req_get_res_parse_content(data):
    # access_token = '[调用鉴权接口获取的token]'
    access_token = get_access_token()
    request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/segmentation/testEx"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': "application/json"}
    response = requests.post(url=request_url, data=data, headers=headers)
    content_dict = json.loads(response.content.decode())
    return content_dict


def compute_IoU_value(pointer_array, detect_mask_array):
    value = (pointer_array & detect_mask_array).sum() / (pointer_array | detect_mask_array).sum()
    return value


if __name__ == "__main__":
    img_path = "./ex02.png"
    encoded_data_str = transform_img_to_req_data(img_path)
    content_dict = send_req_get_res_parse_content(data=encoded_data_str)

    # 保存content_dict为本地文件, 方便后续本地调用调试
    # with open('response_content.json', 'w') as outf:
    #     json.dump(content_dict, outf, ensure_ascii=False)

    # 加载本地json文件
    # filename = 'response_content.json'
    # with open(filename) as f_obj:
    #     content_dict = json.load(f_obj)
    # print(1)

    ########################################
    results = content_dict['results']
    ori_img = cv2.imread(img_path).astype(np.float32)
    height, width = ori_img.shape[:2]

    for item in results:
        if item["name"] == "p":
            rle_obj = {"counts": item['mask'],
                       "size": [height, width]}
            pointer_array = mask_util.decode(rle_obj)
        else:
            continue

    pred_p_at_zone_dict = {}
    alpha = 0.5
    for item in results:
        # Draw bbox
        x1 = int(item["location"]["left"])
        y1 = int(item["location"]["top"])
        w = int(item["location"]["width"])
        h = int(item["location"]["height"])
        x2 = x1 + w
        y2 = y1 + h

        cv2.rectangle(ori_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(ori_img, "{} score: {}".format(item["name"], round(float(item["score"]), 4)), (x1, y1 - 10),
                    cv2.FONT_HERSHEY_PLAIN, 0.7, (255, 255, 255), 1)

        # Draw mask
        rle_obj = {"counts": item['mask'],
                   "size": [height, width]}
        mask = mask_util.decode(rle_obj)

        ####################
        if item["name"] != 'p':
            IoU_value = compute_IoU_value(pointer_array, mask)
            if item["name"] in pred_p_at_zone_dict:
                pred_p_at_zone_dict[item["name"]] = max(IoU_value, pred_p_at_zone_dict[item["name"]])
            else:
                pred_p_at_zone_dict[item["name"]] = IoU_value
        ####################

        new_rle_obj = mask_util.encode(mask)

        random_color = np.array([np.random.random() * 255.0,
                                 np.random.random() * 255.0,
                                 np.random.random() * 255.0])

        idx = np.nonzero(mask)

        ori_img[idx[0], idx[1], :] *= 1.0 - alpha
        ori_img[idx[0], idx[1], :] += alpha * random_color

    print(max(pred_p_at_zone_dict.items(), key=lambda x: x[1]))

    ori_img = ori_img.astype(np.uint8)
    cv2.imshow("img", ori_img)
    cv2.waitKey()
