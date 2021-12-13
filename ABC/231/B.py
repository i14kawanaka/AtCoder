import collections
N = int(input())
l = [input() for _ in range(N)]
c = collections.Counter(l)
print(c.most_common()[0][0])
    