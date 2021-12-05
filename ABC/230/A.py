#N,W = map(int,input().split())
#l = [list(map(int, input().split())) for l in range(N)]
#A,B = map(int,input().split())
N = int(input())

if(9>=N):
    print("AGC00"+str(N))
elif(42<=N):
    print("AGC0"+str(N+1))
else:
    print("AGC0"+str(N))

