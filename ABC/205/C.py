import numpy as np
s1 = input().split()
A = int(s1[0])
B = int(s1[1])
C = int(s1[2])

if(C%2 == 0): #偶数
    if(np.abs(A)==np.abs(B)):
        print("=")
    elif(np.abs(A)>np.abs(B)):
        print(">")
    else:
        print("<")
else:
    if(A==B):
        print("=")
    elif(A>B):
        print(">")
    else:
        print("<")

