fac = [1]
s = 1
for i in range(1, 150):
    s = s * i
    fac.append(s)


def tail(n, m, p):
    s = 0.0
    for i in range(m):
        s += fac[n] / (fac[i] * fac[n - i]) * (p**i) * ((1 - p) ** (n - i))
    return s


def binom(n, m, delta):
    l = 0.0
    r = 1.0
    while abs(r - l) > 1e-15:
        mid = (l + r) / 2
        if tail(n, m, mid) >= delta:
            l = mid
        else:
            r = mid
    return l


print(binom(1000, 260, 0.05))
