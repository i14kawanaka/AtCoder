A,B = map(int,input().split())
A = list(str(A))
B = list(str(B))
A.reverse()
B.reverse()
flag = 0

if(len(A)>len(B)):
    for i in range(len(B)):
        if((int(A[i])+int(B[i]))//10 == 1):
            flag = 1
            print("Hard")
            break
else:
    for i in range(len(A)):
        if((int(A[i])+int(B[i]))//10 == 1):
            flag = 1
            print("Hard")
            break

if(flag == 0):
    print("Easy")