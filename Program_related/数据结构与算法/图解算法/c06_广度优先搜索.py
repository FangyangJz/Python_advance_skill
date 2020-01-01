# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/2 上午1:38
# @Author   : Fangyang
# @Software : PyCharm

from collections import deque


def person_is_seller(person):
    return True if person.endswith('y') else False


def search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == "__main__":
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    result_bool = search(graph, 'you')
