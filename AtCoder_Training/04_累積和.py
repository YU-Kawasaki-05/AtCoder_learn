"""
AtCoder 累積和問題

問題:
長さNの数列A_1, A_2, ..., A_Nがあります。
Q個のクエリが与えられ、各クエリでは区間[L, R]が指定されます。(LからRを加算する) 
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



def my_solution():
    # 入力を受け取る
    N,Q = map(int, input().split())
    if N >= 1 and Q <= 10**5:
        A = list(map(int, input().split())) # A_1, A_2 , ..., A_N ただしA_1 = A[0]
        
        # Aの要素が1以上10^9以下であることを確認
        if min(A) >= 1 and max(A) <= 10**9:
            # [レビュー] 各クエリごとに累積和を計算していると、時間計算量が O(N*Q) になります
            # 事前に累積和を計算しておくと O(N+Q) に改善できます
            
            # [レビュー] 以下のように累積和を前計算するのがベターです
            # cumulative_sum = [0] * (N + 1)
            # for i in range(N):
            #     cumulative_sum[i + 1] = cumulative_sum[i] + A[i]
            
            for i in range(Q):
                L, R = map(int, input().split()) # A[L-1]からA[R-1]までの和を求める
                if 1 <= L <= R <= N:
                    # 累積和を計算
                    # [レビュー] sum(A[L-1:R])は毎回O(N)の計算を行うため非効率です
                    # [レビュー] 前計算した累積和を使えば O(1) で計算できます
                    # [レビュー] 正しくは cumulative_sum[R] - cumulative_sum[L-1]
                    
                    # [レビュー] 問題文では「A_L + A_(L+1) + ... + A_R」となっていますが
                    # 実装では「A[L-1:R]」となっており、Rを含めていません（半開区間）
                    # 問題文の区間は閉区間なので「A[L-1:R]」だとRまでの要素が含まれず誤りです
                    cumulative_sum = sum(A[L-1:R])
                    print(cumulative_sum)
                
            # [レビュー] 制約チェック（if文）の中に処理を書くとインデントが深くなって読みづらくなります
            # AtCoderなどのコンテストでは入力は問題の制約を満たすことが保証されているので
            # 通常は制約チェックは省略しても問題ありません






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
    # my_solution()  # 改善前の解法
    solve()  # 模範解答（効率的な解法）
"""

# [レビューまとめ]
# 1. 累積和の基本概念：各要素までの和を前計算して保存しておくことで、
#    区間の和を O(1) で計算できるようにする手法
#
# 2. 現在のmy_solutionの問題点：
#    - 各クエリごとに sum() を使って計算しているため、時間計算量が O(N*Q)
#    - Q=10^5, N=10^5 の場合、最悪 10^10 回の操作が必要になり、制限時間内に処理できない
#
# 3. 改善方法：
#    - 累積和を前計算しておく（時間計算量 O(N)）
#    - 各クエリでは、累積和を使って O(1) で区間和を計算
#    - 全体の時間計算量は O(N+Q) に改善される
#
# 4. 実装のポイント：
#    - 0から始まるインデックスと1から始まるインデックスの変換に注意
#    - 累積和の配列は長さ N+1 で、cumulative_sum[0]=0 とする
#    - 区間 [L,R] の和は cumulative_sum[R] - cumulative_sum[L-1]
#
# 5. 他の改善点：
#    - 不要な制約チェックを省いてコードをシンプルにする
#    - 問題文の区間定義と実装の整合性を確認する