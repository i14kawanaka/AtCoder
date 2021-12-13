import collections
N,M = map(int,input().split())
A = [0] * M * 2
B = [0] * M
C = [0] * M
for i in range(0,M*2,2):
    A[i], A[i+1] = map(int, input().split())
    B[i//2] = [A[i], A[i+1]]
print(B)


if(M == 0):
    print("Yes")
else:
    ans = collections.Counter(A)
    print(ans)
    ans_1 = []
    ans_2 = []
    if(ans.most_common()[0][1] <= 2):
        for i in range(len(ans)):
            if(ans.most_common()[i][1] == 2):
                ans_2.append(ans.most_common()[i][0])
            else:
                ans_1.append(ans.most_common()[i][0])
        print("ans2",ans_2) 
        print("ans1",ans_1)
    else:
        print("No")

