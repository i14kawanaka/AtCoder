import itertools

s = input()
flag = 0
#print(s[0])
#print(78//10)
aaa =[]
for i in range (0,len(s),1):
    aaa.append(s[i])

for v in itertools.permutations(aaa, 3):
    test = int(v[0]+v[1]+v[2])
    if(test % 2 == 0):
        test_str = str((test // 2))
        if(int(test_str[len(test_str)-2:]) % 4 == 0):
            flag = 1
            break
if(flag != 0 or int(s)==8):
    print("Yes")
else:
    print("No")
    



