# coding=utf-8
import jieba
import os

datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))), 'data')

input_path = os.path.join(datapath, 'pos.txt')
output_path = os.path.join(datapath, 'RES.txt')
# input_path 和 output_path相反的
#stopwords_path = "C:\\Users\\79844\\Desktop\\数据\\train_data600\\病例\\stopwords2.txt"


#stopwords = []
#with open(stopwords_path, 'r', encoding='utf-8') as f:
    #for line in f:
        #if len(line) > 0:
            #stopwords.append(line.strip())
#def tokenizer(s):
    #words = []
    #for word in s:
        #if word not in stopwords:
            #words.append(word)
    #return words

# 读取文件数据，分词，并输出到文件
with open(output_path, 'w', encoding='utf-8') as o:
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            #a = tokenizer(line.strip())
            #b=("".join(a))
            s = line.replace('body', '解剖部位')
            s1 = s.replace('cure', '药物')
            s2 = s1.replace('symp','症状描述')
            s3 = s2.replace( 'dise', '独立症状')
            s4 = s3.replace('chec', '手术' )
            #s5 = s4.replace('\t\t\t','\t')
            o.write(s4+'\n')


