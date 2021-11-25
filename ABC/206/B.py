N = int(input())

aaa = 0
ans = 0
for i in range(1,N,1):
    aaa += i
    if(aaa >= N):
        ans = i
        break
print(ans)

