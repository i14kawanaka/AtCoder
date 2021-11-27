import sys

S = input()
K = int(input())
S = list(S)

ans = 0
cnt = 0
N = K
prev = 0
i = 0
aaa = 0

#for i in range(len(S)):
#    if(S[i] == "X"):
#        aaa = aaa + 1

#if(len(S)<(K+aaa)):
#    print(len(S))
#    sys.exit()

while(i<len(S)):
    if(S[i] == "X"):
        cnt = cnt + 1
        i = i+1
    else:
        if(N > 0):
            N = N - 1
            i = i+1
        elif(ans < cnt+K):
            ans = cnt + K
            prev = prev + 1
            i = prev
            cnt = 0
            N = K
        else:
            prev = prev + 1
            i = prev
            cnt = 0
            N = K
if(ans < cnt+K):
    print(cnt+K)
else:
    print(ans)
        