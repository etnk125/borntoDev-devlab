a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]


def mulmat(a, b):
    if a[1] != b[0]:
        print("Cant calculate !")
    else:
        ma = []
        for r in range(a[0]):
            ma.append([int(i) for i in input().split()])
        mb = []
        for r in range(b[0]):
            mb.append([int(i) for i in input().split()])
        ans = []
        for r in range(a[0]):
            ans.append([])
            for c in range(b[1]):
                sum = 0
                for i in range(a[1]):
                    sum += ma[r][i]*mb[i][c]
                ans[r].append(sum)
        for r in ans:
            print(str(r).replace(',', ''))


mulmat(a, b)
