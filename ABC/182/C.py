s = input() #s_1 s_2を分割して取得し、sに値を入れる

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


aaa = make_divisors(int(s))
for i in range(0, len(aaa), 1):
    print(aaa[i])