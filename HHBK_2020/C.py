import numpy as np
s = input()

s1 = input().split()

aaa = np.zeros(200001)
max_num = 0
for i in range (0,int(s),1):
    #print(i)
    if(aaa[int(s1[i])] == 0):
        aaa[int(s1[i])] = 1
    for ii in range(max_num,200001,1):
        if(aaa[ii] == 0):
            print(ii)
            max_num = ii
            break
