s = input()
s1 = input().split()
 
bbb = 0
goukei = 0
aaa =[]
 
for i in range(0,int(s),1):
    for ii in range(0,len(aaa),1):
        goukei = goukei + aaa[ii]
        #print(goukei)
        if(bbb < goukei):
            bbb = goukei
    goukei = goukei + int(s1[i])
    if(bbb < goukei):
        bbb = goukei
    if(i == 0):
        aaa.append(int(s1[i]))
    else:
        if((aaa[len(aaa)-1]>0 and int(s1[i])>0)or(aaa[len(aaa)-1]<0 and int(s1[i])<0)):
            aaa[len(aaa)-1] = aaa[len(aaa)-1] + int(s1[i])
        else:
            aaa.append(int(s1[i]))
print(bbb)