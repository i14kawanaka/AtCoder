import sys

s = list(map(int,input().split()))

S = s[0]
T = s[1]
X = s[2]

if(T>S):
    for i in range(S,T,1):
        if(i == X):
            print("Yes")
            sys.exit()
    print("No")
else:
    for i in range(S,T+24,1):
        if((i%24) == X):
            print("Yes")
            sys.exit()
    print("No")