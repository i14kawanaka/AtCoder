import numpy as np
s = input().split() #s_1 s_2を分割して取得し、sに値を入れる

#s1 = [input().split() for i in range(2)]
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))
s1 = [input().split() for i in range(int(s[1]))]

print(s)
print(A)
print(B)
print(np.sum(A-B))
print(s1)
aaa = np.zeros(int(s[0]),dtype=np.int64)
if(np.sum(A-B) == 0):
    for i in range(0,int(s[1]),1):
        aaa[int(s1[i][0])-1] += 1 
        aaa[int(s1[i][1])-1] += 1
    print(aaa)
    print(np.argmin(aaa))

else:
    print("No")
