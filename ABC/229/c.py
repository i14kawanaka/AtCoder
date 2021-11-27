import numpy as np

N,W = map(int,input().split())

l = [list(map(int, input().split())) for l in range(N)]
l = sorted(l, reverse=True, key=lambda x: x[0])

omosa = 0
ans = 0
aaa = 0

for i in range(N):
    if(omosa+l[i][1] < W):
        ans = ans + l[i][1]*l[i][0]
        omosa = omosa+l[i][1]
    else:
        aaa = W - omosa
        ans = ans +  l[i][0]*aaa
        break
print(ans)

