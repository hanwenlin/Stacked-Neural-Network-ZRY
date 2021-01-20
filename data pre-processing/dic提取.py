
fp = open(r'C:\Users\hanwenlinPersonal\Desktop\Stacked-Neural-Network-ZRY\data\result.txt',"r",encoding='UTF-8-sig')
fout = open('dic3.txt', 'w',encoding='UTF-8-sig')
str = []
strs = []
for line in fp.readlines():
    for str in line:
        if str=="\t":
            strs.append("\n")
            break
        if not str=="\t":
            strs.append(str)
for line in strs:
    fout.write(line)

print("done")