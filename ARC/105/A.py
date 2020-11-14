s = input().split() #s_1 s_2を分割して取得し、sに値を入れる

#print(s)

sum = 0
sumtest = 0
flag = 0

for i in range(4):
    sum = sum + int(s[i])
    if(sumtest < int(s[i])):
        sumtest = int(s[i])

#sum_half = sum//2

#print(sum_half)

if(sum % 2 == 0):
    if(int(s[0]) == int(s[1])+int(s[2])+int(s[3])):
        flag = 1
    elif(int(s[1]) == int(s[0])+int(s[2])+int(s[3])):
        flag = 1
    elif(int(s[2]) == int(s[0])+int(s[1])+int(s[3])):
        flag = 1
    elif(int(s[3]) == int(s[0])+int(s[1])+int(s[2])):
        flag = 1
    elif(int(s[0])+int(s[1]) == int(s[2])+int(s[3])):
        flag = 1
    elif(int(s[0])+int(s[2]) == int(s[1])+int(s[3])):
        flag = 1
    elif(int(s[0])+int(s[3]) == int(s[1])+int(s[2])):
        flag = 1
    if(flag == 1):
        print("Yes")
    else:
        print("No")
else:
    print("No")

