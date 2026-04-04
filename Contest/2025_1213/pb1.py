N = int(input().strip())
Str = input().strip()
L = len(Str)

if not 2 <= N <= 100 or not 1 <= L <= N:
    exit()

print ("o"*(N-L) + Str)