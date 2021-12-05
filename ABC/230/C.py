N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())


ans=[]

#for i in range(N):
#    ans.append(["."]*N)

left_up = max(1-A,1-B)
right_up = min(N-A,N-B)
left_un = max(1-A,B-N)
right_un = min(N-A,B-1)


#if(left_up > P):
#    left_up = P
#if(right_up > Q):
#    right_up = Q
#if(left_un < R):
#    left_un = R
#if(right_un < S):
#    right_un = S


flag = 0

for i in range(left_up+P-1,right_up+Q-P,1):
    if((1<=(A+i)<(N+1))and(1<=(B+i)<(N+1))):
        flag = 1
        #ans[A+i-1][B+i-1] = "#"
        ans.append([A+i-1,B+i-1])
    elif(flag == 1):
        break

flag = 0
for i in range(left_un,right_un+S-R,1):
    if((1<=(A+i)<(N+1))and(1<=(B-i)<(N+1))):
        flag = 1
        #ans[A+i-1][B-i-1] = "#"
        ans.append([A+i-1,B-i-1])
    elif(flag == 1):
        break

for i in range(P-1,Q,1):
    aaa = ["."]*(S-R+1)
    for ii in range(len(ans)):
        if(ans[ii][0] == i):
            if(R-1 <= ans[ii][1] <= S-1):
                aaa[ans[ii][1]-S] = "#"
    L=''.join(aaa)
    print(L)