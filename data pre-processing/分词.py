# -*- coding=utf8 -*-
import jieba
import re
import codecs
import os, sys

jieba.load_userdict("dic.txt")

datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))), 'data')
fpfile = os.path.join(datapath, 'result.txt')
foutfile = os.path.join(datapath, '分词.txt')
print(datapath)

fp=open(fpfile, 'r', encoding='UTF-8-sig')
fout=open(foutfile, 'w', encoding='UTF-8-sig')
for line in fp.readlines():
    words=jieba.cut(line)
    result=" ".join(words)
    fout.write(result)
