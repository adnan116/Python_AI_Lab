def BubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if(A[j]>A[j+1]):
                c = A[j]
                A[j],A[j+1] = A[j+1],c
    return A
p = [100,2,5]

X = BubbleSort(p)
print(X)

