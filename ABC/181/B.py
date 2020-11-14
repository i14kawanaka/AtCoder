s = input()
s1 = [input().split() for i in range(int(s[0]))]

print(s)
print(s1)

sum = 0

for i in range(0,int(s[0]),1):
    if(int(s1[i][0]) == 1):
        sum_s = 1
    else:
        sum_l = (int(s1[i][1])*(int(s1[i][1])+1))//2
    if(int(s1[i][0]) == 1):
        sum_s = 0
    else:
        sum_s = ((int(s1[i][0])-1)*int(s1[i][0]))//2
    sum = int(sum + sum_l - sum_s)

print(int(sum))

