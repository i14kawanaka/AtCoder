import numpy as np
H,W = map(int,input().split())
l = np.array([list(input()) for l in range(H)])

np.place(l, l == ".", 6)
l = np.pad(l,(1,1),"constant")

def hantei(ii,iii,i):
    a = [0,0,0,0,0,0,0]
    a[int(l[ii-1][iii])] = 1
    a[int(l[ii+1][iii])] = 1
    a[int(l[ii][iii-1])] = 1
    a[int(l[ii][iii+1])] = 1
    return a,a[0]+a[1]+a[2]+a[3]+a[4]+a[5]

def aaa(ii,iii,a):
    for iiii in range(1,7,1):
        if(a[iiii] == 0):
            return iiii

for i in range(4,0,-1):
    print(i)
    for ii in range(1,H+1,1):
        for iii in range(1,W+1,1):
            if(l[ii][iii] == str(6)):
                kai, han = hantei(ii,iii,i)
                if(han >= i):
                    print(ii,iii)
                    l[ii][iii] = aaa(ii,iii,kai)        

for i in range(1,H+1,1):
    L=''.join(l[i][1:W+1])
    print(L)

#L=''.join(aaa)
#    print(L)