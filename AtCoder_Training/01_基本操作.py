"""
AtCoder 基本操作練習問題

問題:
N個の整数が与えられます。その中から最大の整数と最小の整数を見つけて、その差を出力してください。

入力:
1行目: 整数の数 N
2行目: N個の整数 A_1, A_2, ..., A_N

出力:
最大値と最小値の差を出力

制約:
2 <= N <= 100
1 <= A_i <= 1000

入力例1:
5
10 50 30 20 40

出力例1:
40

入力例2:
3
100 100 100

出力例2:
0
"""

def my_solution():

    N = int(input())
    val = list(map(int, input().split()))

    if 2 <= N <= 100 and all(1 <= x <= 1000 for x in val):
        mymax = max(val)
        mymin = min(val)
        print(mymax-mymin)
    else:
        print("Input constraints not met.")



def solve():
    # 整数の数Nを入力
    N = int(input())
    
    # N個の整数を入力
    numbers = list(map(int, input().split()))
    
    # 最大値と最小値を求める
    max_num = max(numbers)
    min_num = min(numbers)
    
    # 差を出力
    print(max_num - min_num)

if __name__ == "__main__":
    solve()
