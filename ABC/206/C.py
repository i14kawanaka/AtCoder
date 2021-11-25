import collections

N = int(input())
A = list(map(int, input().split()))

gokei = 0
l = collections.Counter(A)

for i in range(0,N-1,1):
    c[A[i]] -= 1
    gokei += (N-1-i) - l[A[i]]

print(gokei)





