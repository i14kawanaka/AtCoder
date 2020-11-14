s = input()
s1 = input().split()

aaa = []
flag = 0

for i in range(0,int(s)-1,1):
    if((int(s1[i]) > 0 and int(s1[i+1]) > 0) or (int(s1[i]) < 0 and int(s1[i+1]) < 0)):
        aaa.append(int(s1[i])+int(s1[i+1]))
        i = i + 1
        if(i == int(s)-1):
            flag = 1
    else:
        aaa.append(int(s1[i]))

if(flag == 0):
    aaa.append(int(s1[int(s)-1]))


bbb = 0
goukei = 0
print(aaa)

for i in range(0,len(aaa),1):
    for ii in range(0,i+1,1):
        goukei = goukei + aaa[ii]
        if(bbb < goukei):
            bbb = goukei
print(bbb)

