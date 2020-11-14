import numpy as np

s = input()
s1 = input().split()

arr = np.array([])

for i in range(0,int(s),1):
    arr = np.append(arr,int(s1[i]))
