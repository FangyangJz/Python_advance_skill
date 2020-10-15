#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Datetime :   2020/3/19 上午11:52
@Author   :   Fangyang
"""

import os


def reformat_line(line):
    result_list = []
    add_flag = False

    for ele in line:

        if '[' in ele:
            add_flag = True
            bracket_ele_list = []
        if ']' in ele:
            add_flag = False
            bracket_ele_list.append(ele)
            ele = " ".join(bracket_ele_list)

        if add_flag:
            bracket_ele_list.append(ele)
            continue

        result_list.append(ele)

    return result_list


with open('./kuangge2_test.txt', 'r+') as f:
    context_list = f.readlines()
    # 整理每行文本, 去掉空行, []合成为一个元素
    new_context_list = []
    for line in context_list:
        line_list = line.split()
        line_list = reformat_line(line_list)
        # if line_list:  # 如果不要空行, 这里做if判断, 下行为判断为真时执行
        new_context_list.append(line_list)

    # 重新处理整理后的每行文本
    result_context_list = []
    for line in new_context_list:
        result_without_del_ele_list = []
        for ele in line:
            # 这里自己添加去除条件
            if ('v_abc]' in ele) or ('v_bbc]' in ele):
                continue
            result_without_del_ele_list.append(ele)
        result_context_list.append(result_without_del_ele_list)

    # 重新将list 还原回 str
    result_str = ' \n'.join([' '.join(line) for line in result_context_list])
    # print(1)

with open('./kuangge2_result.txt', 'w+') as f:
    f.write(result_str)

if __name__ == "__main__":
    pass
