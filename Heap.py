n=int(input())
lis = list(map(int,input().split(" ")))
lis.insert(0,-1)
heap=[-1]
for i in range(1,n+1):
    heap.append(lis[i])
    k=i
    while(k//2>0):
        if(heap[k]>heap[k//2]):
            heap[k],heap[k//2]=heap[k//2],heap[k]
            k=k//2
        else:
            break
print(heap[1:])