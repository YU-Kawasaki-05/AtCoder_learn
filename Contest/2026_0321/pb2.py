N = int(input().strip())

# コスト表を 0-indexed で保持する。
# 問題では i < j のみ与えられるため、cost[i][j] (i < j) だけ使う。
cost = [[0] * N for _ in range(N)]

# 入力は上三角部分のみ:
# 1行目: C1,2 ... C1,N
# 2行目: C2,3 ... C2,N
# ...
for i in range(N - 1):
	row = list(map(int, input().split()))
	for offset, value in enumerate(row, start=1):
		j = i + offset
		cost[i][j] = value

# 条件: ある a < b < c で
# C[a][b] + C[b][c] < C[a][c]
# が成り立つかを全探索する。
for a in range(N):
	for b in range(a + 1, N):
		for c in range(b + 1, N):
			# b で分割して乗り継ぐ方が安いなら条件達成
			if cost[a][b] + cost[b][c] < cost[a][c]:
				print("Yes")
				exit()

# 最後まで見つからなければ存在しない
print("No")
