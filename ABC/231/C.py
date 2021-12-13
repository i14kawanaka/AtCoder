import bisect

N,Q = map(int,input().split())
A = list(map(int, input().split()))
l = list(map(int,[input() for _ in range(Q)]))
A.sort()
for i in range(len(l)):
    print(len(A)-int(bisect.bisect_left(A,l[i])))