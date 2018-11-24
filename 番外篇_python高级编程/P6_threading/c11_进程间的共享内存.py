# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/11/18
'''
__author__ = 'Fangyang'


from multiprocessing import Manager, Process


def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == '__main__':
    process_share_dict = Manager().dict()
    first_process = Process(target=add_data, args=(process_share_dict, 'bb', 21))
    second_process = Process(target=add_data, args=(process_share_dict, 'cc', 30))

    first_process.start()
    second_process.start()

    first_process.join()
    second_process.join()

    print(process_share_dict)

