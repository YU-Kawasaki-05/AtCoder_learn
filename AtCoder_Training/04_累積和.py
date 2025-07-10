"""
AtCoder 累積和問題

問題:
長さNの数列A_1, A_2, ..., A_Nがあります。
Q個のクエリが与えられ、各クエリでは区間[L, R]が指定されます。
各クエリに対して、A_L + A_(L+1) + ... + A_Rの値を出力してください。

入力:
1行目: 数列の長さ N とクエリの数 Q
2行目: N個の整数 A_1, A_2, ..., A_N
3行目以降: Q行にわたって、各クエリの L_i と R_i (1-indexed)

出力:
Q行にわたって、各クエリの答えを出力

制約:
1 <= N, Q <= 10^5
1 <= A_i <= 10^9
1 <= L_i <= R_i <= N

入力例:
5 3
1 2 3 4 5
1 3
2 4
3 5

出力例:
6
9
12
"""

def solve():
    # 入力を受け取る
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 累積和を前計算
    cumulative_sum = [0] * (N + 1)
    for i in range(N):
        cumulative_sum[i + 1] = cumulative_sum[i] + A[i]
    
    # クエリを処理
    for _ in range(Q):
        L, R = map(int, input().split())
        # 1-indexedをそのまま使える形に調整
        print(cumulative_sum[R] - cumulative_sum[L - 1])

if __name__ == "__main__":
    solve()
