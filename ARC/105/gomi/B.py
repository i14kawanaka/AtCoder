s = input()
s1 = input().split()
s1_n = []
for i in range(0,int(s),1): 
    s1_n.append(int(s1[i]))

s1_n.sort(reverse=True)

for i in range(0, 1000000000, 1):
    s1_n.sort(reverse=True)
    if(s1_n[0] - s1_n[int(s)-1] == 0):
        break;
    else:
        kotei = s1_n[0]
        s1_n[0] = kotei - s1_n[int(s)-1]
        if(s1_n[1] == kotei):  
            for i in range(1,int(s),1):
                if (s1_n[i] == s1_n[0]):
                    s1_n[i] = kotei - s1_n[int(s)-1]
                else:
                    break;
print(s1_n[0])
