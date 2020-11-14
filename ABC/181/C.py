import numpy as np

s = input() #s_1 s_2を分割して取得し、sに値を入れる
s1 = [input().split() for i in range(int(s[0]))]

ans1 = np.zeros(1000)
ans2 = np.zeros(1000)
ans3 = np.zeros(2000)
flag = 0

for i in range(0,int(s[0]),1):
    ans1[int(s1[i][0])] = ans1[int(s1[i][0])] + 1
    if(ans1[int(s1[i][0])] == 3):
        flag = 1
        break
    ans2[int(s1[i][1])] = ans1[int(s1[i][1])] + 1
    if(ans1[int(s1[i][1])] == 3):
        flag = 1
        break
    ans3[1000+(int(s1[i][0])-int(s1[i][1]))] = ans3[1000+(int(s1[i][0])-int(s1[i][1]))] + 1
    if(ans3[1000+(int(s1[i][0])-int(s1[i][1]))] == 3):
        flag = 1
        break

if(flag == 1):
    print("Yes")
else:
    print("No")