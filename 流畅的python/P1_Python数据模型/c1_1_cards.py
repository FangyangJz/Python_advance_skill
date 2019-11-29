# !/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
created by Fangyang on Time:2018/12/6
'''
__author__ = 'Fangyang'


import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __ppp__(self):
        print(self.ranks)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(len(suit_values))
    print(rank_value * len(suit_values) + suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    # beer_card = Card('7', 'diamonds')
    # print(beer_card)
    #
    deck = FrenchDeck()
    # print(len(deck))
    # print(deck[0], deck[-1])
    #
    # for i in range(3):
    #     print(choice(deck))
    #
    # print(deck[12::13])
    #
    # for card in deck:
    #     print(card)
    #     break
    #
    # for card in reversed(deck):
    #     print(card)
    #     break
    #
    # print(Card('Q', 'hearts') in deck)
    # print('-'*50)
    # for card in sorted(deck, key=spades_high):
    #     print(card)