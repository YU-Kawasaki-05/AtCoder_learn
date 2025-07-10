"""
AtCoder 貪欲法問題

問題:
N枚のコインがあります。コインの種類はA_1, A_2, ..., A_N円です。
合計金額Xを、できるだけ少ないコインの枚数で支払いたいです。
最小で何枚のコインが必要かを求めてください。

入力:
1行目: コインの種類数 N と目標金額 X
2行目: N個のコインの金額 A_1, A_2, ..., A_N (降順にソート済み)

出力:
必要な最小コイン枚数

制約:
1 <= N <= 20
1 <= A_i <= 10^8
A_1 > A_2 > ... > A_N
1 <= X <= 10^9

入力例1:
6 620
500 100 50 10 5 1

出力例1:
6
解説: 500円1枚, 100円1枚, 10円2枚, 1円0枚で620円となる。

入力例2:
4 3
10 5 2 1

出力例2:
2
解説: 2円1枚, 1円1枚で3円となる。
"""

def solve():
    # 入力を受け取る
    N, X = map(int, input().split())
    coins = list(map(int, input().split()))
    
    # 貪欲法でコイン枚数を最小化
    count = 0
    remaining = X
    
    for coin in coins:
        # 現在のコインをできるだけ使う
        used = remaining // coin
        count += used
        remaining -= used * coin
    
    # 結果出力
    print(count)

if __name__ == "__main__":
    solve()
