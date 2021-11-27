s1 = input()
s2 = input()

cnt = 0

for i in range(2):
    if(s1[i] == "#"):
        cnt = cnt+1
    if(s2[i] == "#"):
        cnt = cnt+1

if(cnt != 2):
    print("Yes")
else:
    if(s1[0] == "#" and s2[1] == "#"):
        print("No")
    elif(s1[1] == "#" and s2[0] == "#"):
        print("No")
    else:
        print("Yes")
