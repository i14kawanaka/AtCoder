s = input().split() #s_1 s_2を分割して取得し、sに値を入れる

s1 = [input().split() for i in range(int(s[0]))]
aaa = []
for i in range(0,int(s[0]),1):
    aaa.append(list(s1[i][0]))
count = 0
for i in range(0,int(s[0]),1):
    for ii in range(0, int(s[1]),1):
        if(aaa[i][ii] == "."):
            if(i != int(s[0])-1 and ii != int(s[1])-1):
                if(aaa[i+1][ii] == "."):
                    count = count + 1
                if(aaa[i][ii+1] == "."):
                    count = count + 1
            elif(i == int(s[0])-1 and ii != int(s[1])-1):
                if(aaa[i][ii+1] == "."):
                    count = count + 1
            elif(ii == int(s[1])-1):
                if(i != int(s[0])-1 and aaa[i+1][ii] == "."):
                    count = count + 1
print(count)