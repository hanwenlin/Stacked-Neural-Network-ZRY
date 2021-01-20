import os, sys
import re

datapath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))))

dic1 = os.path.join(os.path.join(datapath,'data'), 'dic.txt')
dic2 = os.path.join(os.path.join(datapath, 'data'), 'dic2.txt')


dicfile1 = {}
dicfile2 = {}



with open(dic1, 'r', encoding='utf-8') as f1:
    count = 0
    for line in f1:
        line = line.strip()
        dicfile1.setdefault(count,[]).append(line)
        if not line:
            count += 1

with open(dic2, 'r', encoding='utf-8') as f1:
    count = 0
    for line in f1:
        line = line.strip()
        dicfile2.setdefault(count,[]).append(line)
        if not line:
            count += 1

for k, v in dicfile2.items():
    if dicfile1.get(k):
        if v != dicfile1.get(k):
            print(k)