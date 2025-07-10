"""
AtCoder 二分探索問題

問題:
N個のボールがあります。i番目のボールの重さはW_iです。
あなたは1つ以上のボールを選び、その重さの合計がちょうどXとなるようにしたいです。
そのような選び方が存在するかどうかを判定してください。

入力:
1行目: ボールの数 N と目標の重さ X
2行目: N個のボールの重さ W_1, W_2, ..., W_N

出力:
選び方が存在する場合は "Yes"、存在しない場合は "No" を出力

制約:
1 <= N <= 20
1 <= X <= 10^6
1 <= W_i <= 10^5

入力例1:
5 12
7 5 3 1 8

出力例1:
Yes
解説: ボール3と5を選ぶと、重さの合計は3+8=11となります。

入力例2:
3 21
6 2 3

出力例2:
No
"""

def solve():
    # 入力を受け取る
    N, X = map(int, input().split())
    weights = list(map(int, input().split()))
    
    # bit全探索
    for bit in range(1, 1 << N):  # 1以上のボールを選ぶため1から開始
        total = 0
        for i in range(N):
            if bit & (1 << i):
                total += weights[i]
        
        if total == X:
            print("Yes")
            return
    
    print("No")

if __name__ == "__main__":
    solve()
