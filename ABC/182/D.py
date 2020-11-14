s = input().split() #s_1 s_2を分割して取得し、sに値を入れる

#print(s)
#print(78//10)

X = int(s[0])
Y = int(s[1])
A = int(s[2])
B = int(s[3])
cnt = 0

for i in range(0,10000000000000000000000, 1):
     #print(X)
    if(X*A < X+B):
        if(X*A < Y):
            X = X*A
            cnt = cnt + 1
        else:
            break
    else:
        if(X+B < Y):
            #print(Y-X)
            aaa = ((Y-X-1) // B)
            #print(aaa)
            cnt = cnt + aaa
        break

print(cnt)


