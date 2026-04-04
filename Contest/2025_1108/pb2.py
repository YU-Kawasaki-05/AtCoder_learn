def function(A, i):
    for j in range(i-1, -1, -1):
        if A[j] > A[i]:
            return j
            break
    return 1000

N = int(input().strip())
A = list(map(int, input().strip().split()))

if 1 <= N <= 100 or not all(1 <= A[i] <= 100 for i in range(N)):
    exit()

for i in range (N):
    if function(A, i) != 1000:
        print(function(A, i)+1)
    else:
        print(-1)


