
def mergeH(n, a, b, pos):
    if pos < n:
        for col in range(n):
            for row in range(n):
                if pos+col < n:
                    a[row][col+pos] += b[row][col]
                else:
                    a[row].append(b[row][col])
    if pos >= n:
        for row in range(n):
            a[row] += [0]*(pos-n)+b[row]


def mergeV(n, a, b, pos):
    if pos < n:
        for row in range(n):
            if row + pos < n:
                for col in range(n):
                    a[row+pos][col] += b[row][col]
            else:
                a += [b[row]]
    if pos >= n:
        a += [[0]*n]*(pos-n)+b


def printList(a):
    for row in a:
        print(" ".join(map(str, row)))


n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = []
for i in range(n):
    b.append(list(map(int, input().split())))

HORIZONTAL = input() == "H"
pos = int(input())
mergeH(n, a, b, pos-1) if HORIZONTAL else mergeV(n, a, b, pos-1)
printList(a)
