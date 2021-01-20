import codecs
import os, sys
import re



datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))), 'data')
infile = os.path.join(datapath, 'pos.txt')
outfile = os.path.join(datapath, 'result.txt')

with open(outfile, 'w', encoding='utf-8') as outf:
    with open(infile, 'r', encoding='utf-8') as infi:
        for line in infi:
            if line:
                # regex = re.compile(' (.+?)/body|/chec|/cure|/symp|/dise ')
                regex = re.compile('( (\S+?)(?:/chec|/body|/symp|/dise|/cure) )')
                t = regex.findall(line)
                for i, j in t:
                    line = line.replace(i, j)
                outf.write(line)
