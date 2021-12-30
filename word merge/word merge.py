
a = []
n = int(input())
for i in range(n):
    word = input().split()
    a.append(word)
ans = a[0]
a.remove(a[0])

for k in range(n-1):
    for i in a:
        head = -1
        tail = -1
        for j in range(min(len(i), len(ans))):
            if i[:j] == ans[-1*j:]:
                tail = j
                break
            if i[-1*j:] == ans[:j]:
                head = j
                break
        if tail != (-1):
            ans += i[tail:]
            a.remove(i)
            break
        if head != (-1):
            ans = i[:-1*head]+ans
            a.remove(i)
            break
print(" ".join(ans))
