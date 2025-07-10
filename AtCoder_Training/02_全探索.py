"""
AtCoder 全探索問題

問題:
1以上N以下の整数の中で、10進法で各桁の和がA以上B以下であるものの総和を求めてください。

入力:
N A B

出力:
条件を満たす整数の総和

制約:
1 <= N <= 10000
1 <= A <= B <= 36

入力例1:
20 2 5

出力例1:
84
解説: 2+3+4+5+6+7+8+9+10+11+19=84

入力例2:
100 4 16

出力例2:
4554
"""

def digit_sum(n):
    """整数nの各桁の和を計算する関数"""
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def solve():
    # 入力を受け取る
    N, A, B = map(int, input().split())
    
    # 条件を満たす整数の総和を計算
    total = 0
    for i in range(1, N + 1):
        sum_digits = digit_sum(i)
        if A <= sum_digits <= B:
            total += i
    
    # 結果を出力
    print(total)

if __name__ == "__main__":
    solve()
