# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Datetime : 2019/12/8 下午5:38
# @Author   : Fangyang
# @Software : PyCharm


import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as tud

from collections import Counter
import numpy as np
import random
import math

import pandas as pd
import scipy
import sklearn
from sklearn.metrics.pairwise import cosine_similarity

random.seed(1)
np.random.seed(1)
torch.manual_seed(1)

# 设定一些超参数
C = 3  # contect window
K = 100  # number of negative samples
NUM_EPOCHS = 2
MAX_VOCAB_SIZE = 30000
BATCH_SIZE = 128
LEARNING_RATE = 0.2
EMBEDDING_SIZE = 100


def word_tokenize(text):
    return text.split()


train_data_path = "./7月在线_text8_pytorch_word_vector_data/text8.train.txt"
with open(train_data_path, 'r') as fin:
    text = fin.read()

text = text.split()
vocab = dict(Counter(text).most_common(MAX_VOCAB_SIZE - 1))
vocab['<unk>'] = len(text) - np.sum(list(vocab.values()))
# print(vocab['<unk>'])

idx_to_word = [word for word in vocab.keys()]
word_to_idx = {word: i for i, word in enumerate(idx_to_word)}

word_counts = np.array([count for count in vocab.values()], dtype=np.float32)
word_freqs = word_counts / np.sum(word_counts)
word_freqs = word_freqs ** (3. / 4.)
word_freqs = word_freqs / np.sum(word_freqs)
VOCAB_SIZE = len(idx_to_word)
print(1)


class WordEmbeddingDataset(tud.Dataset):
    def __init__(self, text, word_to_idx, idx_to_word, word_freqs, word_counts):
        super(WordEmbeddingDataset, self).__init__()
        self.text_encoded = [word_to_idx.get(word, word_to_idx['<unk>']) for word in text]
        self.text_encoded = torch.LongTensor(self.text_encoded)
        self.word_to_idx = word_to_idx
        self.idx_to_word = idx_to_word
        self.word_freqs = torch.Tensor(word_freqs)
        self.word_counts = word_counts

    def __len__(self):
        # 这个数据集有多少个item
        return len(self.text_encoded)

    def __getitem__(self, idx):
        center_word = self.text_encoded[idx]
        pos_indices = list(range(idx - C)) + list(range(idx + 1, idx + C + 1))  # window内单词的index
        pos_indices = [i % len(self.text_encoded) for i in pos_indices]  # 取余, 防止超出text长度
        pos_words = self.text_encoded[pos_indices]  # 周围单词
        neg_words = torch.multinomial(self.word_freqs, K * pos_words.shape[0], True)  # 负例采样单词
        return center_word, pos_words, neg_words


dataset = WordEmbeddingDataset(text, word_to_idx, idx_to_word, word_freqs, word_counts)
dataloader = tud.DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=2)

# for i, (center_word, pos_words, neg_words) in enumerate(dataloader):
#     print(i)

class EmbeddingModel(nn.Module):
    def __init__(self):
        pass




if __name__ == '__main__':
    pass
