# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/11/26 下午3:18
# @Author   : Fangyang
# @Software : PyCharm


import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms
from lenet5 import LeNet5


def main():
    batch_size = 32

    cifar_train = datasets.CIFAR10(
        'cifar',
        train=True,
        transform=transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor()
        ])
    )
    cifar_train = DataLoader(dataset=cifar_train, batch_size=batch_size, shuffle=True)

    cifar_test = datasets.CIFAR10(
        'cifar',
        train=False,
        transform=transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor()
        ]),
    )
    cifar_test = DataLoader(dataset=cifar_test, batch_size=batch_size, shuffle=True)

    # x, label = iter(cifar_train).next()
    # print(1)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = LeNet5().to(device)
    print(model)
    criteron = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)
    for epoch in range(100):
        model.train()
        for batch_id, (x, label) in enumerate(cifar_train):
            x, label = x.to(device), label.to(device)
            logits = model(x)
            loss = criteron(logits, label)

            # backpropagation
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(epoch, loss.item(), type(loss.item()))

        model.eval()
        with torch.no_grad():
            # test
            total_correct = 0
            total_num = 0
            for x, label in cifar_test:
                x, label = x.to(device), label.to(device)
                logits = model(x)
                pred = logits.argmax(dim=1)
                total_correct += torch.eq(pred, label).float().sum().item()
                total_num += x.size(0)

            acc = total_correct/total_num
            print(f'epoch:{epoch}, acc:{acc}')


if __name__ == '__main__':
    main()
