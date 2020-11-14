import numpy as np

s = input()
s1 = input().split()
s1_na = np.array([], dtype=np.int64)
for i in range(0,int(s),1): 
    s1_na = np.append(s1_na,int(s1[i]))

while True:
    max_kotei = np.max(s1_na)
    max_kari = max_kotei-np.min(s1_na)
    
    if(max_kari==0):
        break;
    else:
        while True:   
            aaa = np.argmax(s1_na)
            if(s1_na[aaa] == max_kotei):
                s1_na[aaa] = max_kari
            else:
                break;
print(np.max(s1_na))



