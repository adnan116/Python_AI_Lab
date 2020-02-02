def CountingSort(A):

    C = [0] * len(A)
        
    for j in range(1,len(A)):
        C[A[j]] = C[A[j]]+1

    for i in range(1,len(A)):
        C[i] = C[i] + C[i-1]

    for j in range(len(A),1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1

S = [4,3,8]
print(CountingSort(S))
