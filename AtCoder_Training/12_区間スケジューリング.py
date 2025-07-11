"""
AtCoder 区間スケジューリング問題

問題:
N個の仕事があります。各仕事iは開始時刻S_i、終了時刻T_iで表されます。
1つの仕事を行っている間は、他の仕事を行うことはできません。
最大でいくつの仕事をこなせるか求めてください。

入力:
1行目: 仕事の数 N
2行目: 各仕事の開始時刻 S_1, S_2, ..., S_N
3行目: 各仕事の終了時刻 T_1, T_2, ..., T_N

出力:
最大でこなせる仕事の数

制約:
1 <= N <= 10^5
1 <= S_i < T_i <= 10^9

入力例1:
5
1 2 4 6 8
3 5 7 9 10

出力例1:
3
解説: 仕事1(1-3)、仕事3(4-7)、仕事5(8-10)を選ぶと3つの仕事をこなせます。

入力例2:
3
1 2 3
4 5 6

出力例2:
3
解説: すべての仕事をこなすことができます。
"""

def mysolution():
    # 実装を試みてください
    pass

"""
def solve():
    # 入力を受け取る
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    
    # 仕事をタプル(終了時刻, 開始時刻)の形で格納し、終了時刻でソート
    jobs = sorted(zip(T, S))
    
    count = 0      # 選んだ仕事の数
    current_end = 0  # 現在選んでいる仕事の終了時刻
    
    # 終了時刻が早い順に貪欲に選んでいく
    for end, start in jobs:
        # 次の仕事の開始時刻が、現在の仕事の終了時刻以降であれば選べる
        if start >= current_end:
            count += 1
            current_end = end
    
    print(count)


if __name__ == "__main__":
    solve()
"""
