def sum_array(A, l, r):
    return sum(A[l-1:r])

def func1(A, l, r):
    SN = sum_array(A, l, r)
    for k in range (l, r+1):
        if SN%A[k-1] == 0:
            return True #約数ならTrue
            break
    return False


N = int(input().strip())
A = list(map(int, input().strip().split()))

if not 1 <= N <= 50:
    exit()

for i in range(N):
    if not A[i] % 1 == 0 or A [i] < 1 or A[i] > 1000:
        exit()

counter = 0

for i in range(1, N+1): #0~N
    for j in range(i, N+1): #i~N
        if func1(A, i, j) == False:
            counter += 1

print(counter)
