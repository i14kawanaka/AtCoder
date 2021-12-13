import sys
A = input()
B = input()

if(int(B)%2==1):  
    B = str(int(int(B)*10)//2)
else:
    B = str((int(B))//2)
print(A+"0"+B)



"""
if(B in bbb):
    print(A)
else:
    for i in range(len(aaa),18,1):       
        for ii in range(0,10**(18-len(aaa)),1):
            if(B in str(int(aaa+str(ii))*2)):
                print(aaa+str(ii))
                sys.exit()
"""
            