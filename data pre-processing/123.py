import codecs
import os, sys


datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))), 'data')
print(datapath)


ccksES2018 = os.path.join(datapath, 'ccks2018ES.txt')
ccks2018 = os.path.join(datapath, 'ccks2018.txt')
input_data = codecs.open(ccksES2018, "r", encoding="UTF-8-sig")
output_data = codecs.open(ccks2018, "w", encoding="UTF-8-sig")
for line in input_data.readlines():
    word_list = line.strip().split()
