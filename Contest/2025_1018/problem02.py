N, K = map(int, input().split())
S = input().strip()

string = [''] * (N - K + 1)

for i in range(N-K+1):
    string[i] = S[i:i+K]

# 各部分文字列の出現回数をカウント
from collections import Counter
count = Counter(string)

x = max(count.values()) #x=max_n

# 出現回数が最大の文字列を辞書順でソート
sorted_answers = sorted([s for s, c in count.items() if c == x])

# 最大値を出力
print(x)
# 各文字列を1行ずつ出力
for ans in sorted_answers:
    print(ans)