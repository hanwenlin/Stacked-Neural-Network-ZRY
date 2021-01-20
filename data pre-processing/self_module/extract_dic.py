import codecs
import os, sys
import re

datapath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))))

posfile = os.path.join(os.path.join(datapath,'data'), 'pos.txt')
dic_file = os.path.join(os.path.join(datapath, 'data'), 'dic2.txt')


# regx = re.compile(' (\S+?)/')
regx = re.compile(' (\S+?)\s?/(?=body|symp|cure|dise|chec)')
with open(posfile, 'r', encoding='utf-8') as f1:
    with open(dic_file, 'w', encoding='utf-8') as f2:
        for line in f1:
            line = line.rstrip()
            if line:
                d = regx.findall(line)
                f2.write('\n'.join(d))
                f2.write('\n\n')

