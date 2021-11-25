import numpy as np
s1 = input().split()
N = int(s1[0])
Q = int(s1[1])

A = list(map(int, input().split()))
A = np.array(A)

K = []
for _ in range(Q):
    K.append(int(input()))
K = np.array(K)

indices = [*range(len(K))]
sorted_indices = sorted(indices, key=lambda i: -K[i], reverse=True)
K = np.array([K[i] for i in sorted_indices])
gokei=np.zeros(Q)
ans = []

for i in range(Q):
    if(i == 0):
        gokei[i] = 0
    else:
        gokei[i] = gokei[i-1]
    tmp = 0
    for ii in range(200000000000):
        gokei[i] = gokei[i] + tmp
        ind = np.where(A[int(gokei[i]):] <= K[i]+gokei[i])
        tmp = len(ind[0])
        if(tmp== 0):
            ans.append(K[i]+gokei[i])
            break
for i in range(Q):
    print(int(ans[sorted_indices[i]]))