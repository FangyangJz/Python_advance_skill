# 创建一个容量为n的双端队列
from collections import deque
from random import randint

hist_q = deque([], 5)
target = randint(1, 100) 
while True:
    guess = input('请输入一个1-100的数字:')
    if guess.isdigit():
        guess = int(guess)
        hist_q.append(guess)
        if guess == target:
            print('right!')
            break
        elif guess < target:
            print('小了, 再往大了猜')
        else:
            print('大了, 往小猜')
    elif guess == 'quit':
        break
    elif guess == 'h?':
        print(hist_q)