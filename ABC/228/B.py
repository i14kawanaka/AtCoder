import sys
N, X = map(int, input().split())
A = list(map(int,input().split()))

ans = 1
ans_list = []
ans_list.append(X)
flag = 0

for i in range(0,N,1):
    aaa = len(ans_list)
    bbb = A[ans_list[aaa-1]-1]
    for ii in range(0,aaa,1):
        if(ans_list[ii] == bbb):
            print(ans)
            sys.exit()
    if(flag == 0):
        ans_list.append(A[ans_list[i]-1])
        ans = ans + 1
    else:
        print(ans)