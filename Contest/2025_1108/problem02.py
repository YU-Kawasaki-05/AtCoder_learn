X = input().strip()
N = input().strip()

w = list(input().split())

if 1 >= X >= 100 or 1 >= N >= 100:
    exit()

for i in range(len(w)):
    if 1 >= w[i] > 100:
        exit()
    
Q = input().strip()

for i in range(Q):
    