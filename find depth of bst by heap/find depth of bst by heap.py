from math import log2, ceil
heap = {}


def addNode(data, pos=1):
    if heap.get(pos) == None:
        heap[pos] = data
    else:
        if data < heap[pos]:
            addNode(data, pos*2)
        else:
            addNode(data, pos*2+1)


for i in range(int(input())):
    addNode(int(input()))
print(ceil(log2(max(heap.keys())+1)))
