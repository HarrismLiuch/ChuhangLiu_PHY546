# 04-Q6
__author__ = "Chuhang Liu"

import matplotlib.pyplot as plt
import numpy as np

#Read the file and create the dictionaty {'word':count}
f = open("shore_leave.txt", "r")
string = ''
for line in f:
    string = string + ' ' + line

string = string.replace(",","").replace(".","").replace("--","")
st = string.split()
for i in range(len(st)):
    st[i] = st[i].lower()
Dict = {}
for i in st:
    if (i in Dict.keys()) == True:
        Dict[i] += 1
    if (i in Dict.keys()) == False:
        Dict[i] = 0
        Dict[i] += 1
# sort through value
Sort = sorted(Dict.items(), key=lambda e:e[1], reverse=True)

# frequency-word plot

# create x,y,xticks1. Length = bar numbers
x=np.arange(25)+1
y = np.zeros(25)
xticks1 = list(range(25))
# give value to y and xticks1
for i in range(25):
    y[i] = Sort[i][1]
    xticks1[i] = Sort[i][0]
# create a bar plot
plt.bar(x,y,width = 0.35,align='center',color = 'c',alpha=0.8)
# change xticks
plt.xticks(x,xticks1,size='large',rotation=30)
# create label
plt.xlabel('Word')
plt.ylabel('Frequency')
# set number label
for a,b in zip(x,y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)
# set image size
f = plt.gcf()
f.set_size_inches(16,12)
