"""
N = int(input().strip())

A = [[None for i in range(N)] for j in range(N)]

#print(A)
lim = N*N - 1

if not 3 <= N <= 99 or not N % 2 == 1:
    exit()


def fill(A, r, c, k, l):
    if A[(r-1)%N][(c+1)%N] is None and l > 0:
        A[(r-1)%N][(c+1)%N] = k+1
        l -= 1
        fill(A, (r-1)%N, (c+1)%N, k+1, l)
        
    elif l > 0:
        A[(r+1)%N][c] = k+1
        l -= 1
        fill(A, (r+1)%N, c, k+1, l)
        
    return A

A[0][(N-1)//2] = 1

fill(A, 0, (N-1)//2, 1, lim)

#print(A)

for row in A:
    print(*row)
"""

"""
N = int(input().strip())

A = [[None for i in range(N)] for j in range(N)]

#print(A)

def fill(A, r, c, k):
    if A[(r-1)%N + 1][(c+1)%N + 1] is None:
        A[(r-1)%N + 1][(c+1)%N + 1] = k+1
        fill(A, (r-1)%N, (c+1)%N, k+1)
    else:
        A[(r+1)%N+1][c+1] = k+1
        fill(A, (r+1)%N, c, k+1)
    return A

A[0][(N-1)//2] = 1

fill(A, 0, (N-1)//2, 1)

print(A)

"""

N = int(input().strip())

if not (3 <= N <= 99) or N % 2 == 0:
    exit()

A = [[None] * N for _ in range(N)]

r = 0
c = (N - 1) // 2
A[r][c] = 1

for k in range(1, N * N):
    nr = (r - 1) % N
    nc = (c + 1) % N

    if A[nr][nc] is None:
        r, c = nr, nc
    else:
        r = (r + 1) % N

    A[r][c] = k + 1

for row in A:
    print(*row)
