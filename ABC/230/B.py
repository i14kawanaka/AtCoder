S = input()

T=(len(S))*("oxx")
flag = 0
for i in range(3):
    if(S == T[i:len(S)+i]):
        flag = 1
        print("Yes")
        break
if(flag == 0):
    print("No")


