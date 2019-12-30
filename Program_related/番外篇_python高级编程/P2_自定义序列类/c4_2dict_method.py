# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/9/14
'''
__author__ = 'Fangyang'

if __name__ == '__main__':
    # dict #ctrl+enter进去看
    # a = {
    #     'b1': {'company': 'imooc'},
    #     'b2': {'company': 'ic2'}
    # }
    # a.clear()
    new_list = ['b','c']
    new_dict = dict.fromkeys(new_list, {'com': 'value'})
    print(new_dict)

    print(new_dict.get('d', 'emmmpty'))

    default_value = new_dict.setdefault('bbbb', 'default_value')

    new_dict.update({'d22':'22'})
    new_dict.update(boddy='imm', b=22)
    new_dict.update([('listkey', 'listvalue')])
    new_dict.update((('tupkey', 'tupvalue'), ('tt', 222)))
    pass


