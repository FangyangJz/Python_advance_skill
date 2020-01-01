# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2020/1/1 下午3:25
# @Author   : Fangyang
# @Software : PyCharm
import random
import copy


class MainBox:
    def __init__(self, deep=3):
        self.item = []
        self.max_deep = deep
        self.current_deep = deep

    def make_a_pile_to_look_through(self):
        if self.current_deep == 0 | self.max_deep == 0:
            return self
        else:
            for i in range(self.max_deep):
                print(f"step {i}, current deep is {self.current_deep}/{self.max_deep}")
                if random.random() < 0.1:
                    self.item.extend(["key"])
                    self.max_deep = 0
                    print(f"key in {self.current_deep}/{self.max_deep}")
                else:
                    item = MainBox(self.current_deep - 1).make_a_pile_to_look_through()
                    self.item.extend([item])
            return self

    def grab_a_item(self):
        select_index = random.randint(0, len(self.item) - 1)
        return_item = self.item[select_index]
        self.item.pop(select_index)
        return return_item


def look_for_key(pile):
    while pile.item:
        item = pile.grab_a_item()
        if isinstance(item, MainBox):
            continue
        elif item == "key":
            print(f"Found the key! It'in {pile.current_deep, pile.max_deep}")
            return
    print("There is no key in the pile")


def look_for_key_recursive(pile):
    while pile.item:
        item = pile.grab_a_item()
        if isinstance(item, MainBox):
            look_for_key_recursive(item)
        elif item == "key":
            print(f"Found the key! It'in {pile.current_deep, pile.max_deep}")
            return
    print("There is no key in the pile")


if __name__ == "__main__":
    main_box = MainBox()
    pile = main_box.make_a_pile_to_look_through()
    pile2 = copy.deepcopy(pile)
    look_for_key(pile)
    print("=" * 50)
    look_for_key_recursive(pile2)
    print(1)
