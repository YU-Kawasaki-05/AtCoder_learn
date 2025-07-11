"""
動的計画法（DP）の補足コードと解説

このファイルでは、動的計画法の基本的な実装例から発展的な問題までを実装します。
初心者が理解しやすいように、各ステップでの状態変化も表示するようにしています。
"""

def print_dp_table(dp, step_info=""):
    """DP表の内容を見やすく表示する補助関数"""
    print(f"--- {step_info} ---")
    for i, value in enumerate(dp):
        print(f"dp[{i}] = {value}")
    print()

# 1. 基本的な階段上りの問題
def stairs_dp_with_trace(N):
    """
    N段の階段を1段または2段で上る方法の数を求め、途中経過も表示
    """
    # DPテーブル初期化
    dp = [0] * (N + 1)
    dp[0] = 1  # 0段目には1通りでたどり着ける
    
    print_dp_table(dp, "初期状態")
    
    # ボトムアップでDP
    for i in range(N):
        # i+1段目に行く
        if i + 1 <= N:
            dp[i + 1] += dp[i]
            print(f"i={i}: {i}段目から{i+1}段目へ移動 → dp[{i+1}] = {dp[i+1]}")
        
        # i+2段目に行く
        if i + 2 <= N:
            dp[i + 2] += dp[i]
            print(f"i={i}: {i}段目から{i+2}段目へ移動 → dp[{i+2}] = {dp[i+2]}")
    
    print_dp_table(dp, "最終状態")
    return dp[N]

# 2. メモ化再帰版（トップダウンアプローチ）の階段問題
def stairs_dp_memo(N, memo=None):
    """
    メモ化再帰を使った階段上り問題の解法
    """
    if memo is None:
        memo = {0: 1, 1: 1}
        
    if N in memo:
        return memo[N]
    
    # N段目に来る方法は、N-1段目からの1段上りとN-2段目からの2段上り
    memo[N] = stairs_dp_memo(N-1, memo) + stairs_dp_memo(N-2, memo)
    return memo[N]

# 3. コイン問題（応用問題）
def coin_problem_with_trace(coins, X):
    """
    コインを使って合計X円を作る方法の数を求め、途中経過も表示
    """
    dp = [0] * (X + 1)
    dp[0] = 1  # 0円を作る方法は1通り
    
    print_dp_table(dp[:10], "初期状態（最初の10要素）")
    
    for coin in coins:
        print(f"コイン {coin} 円を使う場合：")
        for i in range(coin, X + 1):
            dp[i] += dp[i - coin]
            if i < 10:  # 状態変化の例として最初の10要素だけ表示
                print(f"dp[{i}] += dp[{i-coin}] → {dp[i-coin]}通りを追加 → dp[{i}] = {dp[i]}")
        
        print_dp_table(dp[:10], f"コイン {coin} 円を使った後（最初の10要素）")
    
    return dp[X]

# 4. ナップサック問題
def knapsack_with_trace(weights, values, capacity):
    """
    ナップサック問題を解き、途中経過も表示
    weights: 各アイテムの重さのリスト
    values: 各アイテムの価値のリスト
    capacity: ナップサックの容量
    """
    n = len(weights)
    # DPテーブル初期化 dp[i][w] = 最初のiアイテムから選んで、重さw以下の最大価値
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    print("初期状態:")
    for i in range(n + 1):
        print(f"dp[{i}] = {dp[i]}")
    print()
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # アイテムi-1を入れない場合
            dp[i][w] = dp[i-1][w]
            
            # アイテムi-1を入れる場合（重さの制約を満たす場合）
            if w >= weights[i-1]:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
        
        print(f"アイテム{i}（重さ={weights[i-1]}, 価値={values[i-1]}）を考慮した後:")
        for j in range(n + 1):
            print(f"dp[{j}] = {dp[j]}")
        print()
    
    return dp[n][capacity]

# 5. 最長増加部分列（LIS）
def lis_with_trace(arr):
    """
    最長増加部分列の長さを求め、途中経過も表示
    """
    n = len(arr)
    dp = [1] * n  # dp[i] = arr[i]で終わる最長増加部分列の長さ
    
    print(f"配列: {arr}")
    print_dp_table(dp, "初期状態")
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                print(f"arr[{i}]={arr[i]} > arr[{j}]={arr[j]} なので、dp[{i}] = max({dp[i]}, dp[{j}] + 1) = {dp[i]}")
        
        print_dp_table(dp, f"i={i}の処理後")
    
    return max(dp)

# 実行例
if __name__ == "__main__":
    print("==== 階段上り問題（ボトムアップDP） ====")
    result = stairs_dp_with_trace(5)
    print(f"結果: 5段の階段を上る方法は {result} 通りあります。\n")
    
    print("==== 階段上り問題（メモ化再帰） ====")
    result = stairs_dp_memo(5)
    print(f"結果: 5段の階段を上る方法は {result} 通りあります。\n")
    
    print("==== コイン問題 ====")
    coins = [1, 5, 10]
    X = 15
    result = coin_problem_with_trace(coins, X)
    print(f"結果: {coins}を使って{X}円を作る方法は {result} 通りあります。\n")
    
    print("==== ナップサック問題 ====")
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    result = knapsack_with_trace(weights, values, capacity)
    print(f"結果: 容量{capacity}のナップサックに入れられる最大価値は {result} です。\n")
    
    print("==== 最長増加部分列（LIS）====")
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    result = lis_with_trace(arr)
    print(f"結果: 配列{arr}の最長増加部分列の長さは {result} です。\n")
