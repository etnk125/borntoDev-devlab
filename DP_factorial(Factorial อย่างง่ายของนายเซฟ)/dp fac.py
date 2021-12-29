f = {}


def fac(n):
    if n >= 0:
        f[0] = 1
        for i in range(1, n+1):
            f[i] = f[i-1]*i
    return f[n]


n = int(input()[1:-1])
print(str(n)+'!:'+str(fac(n)))
