import numpy as np

s = input()
s1 = input().split()

aaa = np.array(s1)
#print(aaa)

an1 = 0
an2 = 0
an3 = 0

for i in range(0, int(s), 1):
    an1 = an1 + np.abs(int(aaa[i]))
    an2 = an2 + int(aaa[i])**2
    if(an3 < np.abs(int(aaa[i]))):
        an3 = np.abs(int(aaa[i]))

print(an1)
print(np.sqrt(an2))
print(an3)

