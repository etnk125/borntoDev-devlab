q = []
n = int(input())
if n >= 2:
    q.append(2)
for i in range(3, n+1, 2):
    index = True
    for j in q:
        if i % j == 0:
            index = False
            break
    if index:
        q.append(i)
print(q)
