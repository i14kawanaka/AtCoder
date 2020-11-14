import numpy as np

def big(a, b):
    if(a > b):
        return a
    return b

def small(a, b):
    if(a > b):
        return b
    return a

def bbb(a,b):
    if(a>b):
        return (a-b+1)**2
    return(b-a+1)**2

def sisumi(a,b):
    if(a>b):
        return (a-b+1)

def abs(a):
    if(a>0):
        return a
    else:
        return -a

s = input()

s1 = [input().split() for i in range(int(s[0]))]

si = []
for i in range(0,int(s),1):
    si.append([int(s1[i][0]),int(s1[i][1]),int(s1[i][2])])
print(si)

for i in range(0,int(s),1):
    zentai = bbb(si[i][0],si[i][1])*bbb(si[i][0],si[i][2])
    kaburi_zentai = ((big(si[i][1],si[i][2])+(small(si[i][1],si[i][2])-1))**2)*bbb(si[i][0],big(si[i][1],si[i][2]))
    kaburi_hoten_1 = ((big(si[i][1],si[i][2])+(small(si[i][1],si[i][2])-1))**2) - big(si[i][1],si[i][2])**2
    #kaburi_hoten_2 = ((big(si[i][1],si[i][2])+(small(si[i][1],si[i][2])-1))**2) - (big(si[i][1],si[i][2])+(small(si[i][1],si[i][2])-1))
    kaburi_hoten_2 = (big(si[i][1],si[i][2])+(small(si[i][1],si[i][2])-1))
    flag = si[i][0]-big(si[i][1],si[i][2])-small(si[i][1],si[i][2])
    if(flag => 0):
        kaburi_hoten_3 = 0
    else:
        kaburi_hoten_3 = 




    print(zentai)
    print(kaburi_zentai)
    print(kaburi_hoten_1)
    print(kaburi_hoten_2)
    print((si[i][0]-big(si[i][1],si[i][2])-1)*4)
    print((zentai-(kaburi_zentai-(kaburi_hoten_1*4+kaburi_hoten_2*4*(si[i][0]-big(si[i][1],si[i][2])-1))))%1000000007)

#for i in range(0,int(s),1):
#    aaa = (int(s1[i][0])-int(s1[i][1])+1)*(int(s1[i][0])-int(s1[i][1])+1)*(int(s1[i][0])-int(s1[i][2])+1)*(int(s1[i][0])-int(s1[i][2])+1)-((bigman(s1[i][1],s1[i][2])-smallman(s1[i][1],s1[i][2])+1)**2*(int(s1[i][0])-bigman(s1[i][1],s1[i][2])+1)**2)
#    #print((bigman(s1[i][1],s1[i][2])-smallman(s1[i][1],s1[i][2])+1)**2)
#    print(((int(s1[i][0])-bigman(s1[i][1],s1[i][2])+1)**2))
#    print(aaa%1000000007)
