r = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}
ans = ""
n = int(input())
for i in r.keys():
    cd = 3
    while n >= i and cd != 0:
        n -= i
        cd -= 1
        ans += r[i]
print(ans)
