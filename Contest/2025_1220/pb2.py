H, W, N = map(int, input().strip().split())

grid = [list(map(int, input().strip().split())) for _ in range(H)]

B = [0]*N #B1はB[0], BnはB[N-1]
count = [0]*H

for i in range(N):
    B[i] = int(input().strip())

#########
n = len(B)
if not 1<= H <=3 or not 1<= W <= 5 or not 1 <= N <= 90 or not all(1 <= grid[_][x] <= 90 for _ in range(H) for x in range(W)) or not all(1 <= B[i] <= 90 for i in range(N)):
    exit()
elif len(set(B)) != n:
    exit()

for _ in range(H):
    for x in grid[_]:
        if x in B:
            count[_] += 1

print(str(max(count)))