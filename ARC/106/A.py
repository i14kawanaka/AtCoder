s = input()

N = int(s)
flag = 0

for i in range(1, 39, 1):
    for ii in range(1, 27, 1):
        if(3**i+5**ii==N):
            ans1 = i
            ans2 = ii
            flag = 1 
            break
    print(i)
if(flag == 0):
    print("-1")
else:
    print(ans1,ans2)
        

