import numpy as np
import itertools

s = input() #s_1 s_2を分割して取得し、sに値を入れる
flag = 0

N = list(map(int, s))

#print(N)
#print(len(N))

for i in range(0, len(N),1):
    for v in itertools.combinations(N, len(N)-i):
        if(sum(v) % 3 == 0):
            print(i)
            flag = 1
            break
    if(flag == 1):
        break


if(flag == 0):
    print("-1")


