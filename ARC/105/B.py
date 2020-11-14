import math

s = input()
s1 = input().split()
s1_n = []
for i in range(0,int(s),1): 
    s1_n.append(int(s1[i]))

s1_n.sort(reverse=True)

gcd_now = s1_n[0]
for i in range(1, len(s1_n), 1):
    gcd_now = math.gcd(gcd_now,s1_n[i])
print(gcd_now)
