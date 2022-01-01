fac = list()


def cnrMod(n, r, p):
    return int((fac[n]*pow(fac[n-r], p-2, p)) % p*pow(fac[r], p-2, p)) % p


def fMod(n, fac, p):
    fac += [1]
    for i in range(1, n+1):
        fac += [(i % p*fac[i-1]) % p]


n, m = [int(i) for i in input().split()]
p = 1000000007
count = n
s = 0
i = 0
fMod(n, fac, p)
while count >= 0:
    x = cnrMod(n, i, p)
    s += x
    # print(n,i,x,s)
    i += 1
    n -= (m-1)
    count -= m
    s %= p
# print(cnr(69,0))
print(s)
