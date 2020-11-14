import numpy as np

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


s = input()
s1 = input().split()
bbb = np.zeros(1001)
for i in range(0,int(s),1):
    aaa = make_divisors(int(s1[i]))
    #print(aaa)
    for ii in range(1,len(aaa), 1):
        bbb[aaa[ii]] = bbb[aaa[ii]] + 1

print(int(np.argmax(bbb)))