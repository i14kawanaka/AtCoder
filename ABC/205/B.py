s = int(input())
l = list(map(int, input().split()))

if(len(l) == len(list(set(l))) ):
    print("Yes")
else:
    print("No")