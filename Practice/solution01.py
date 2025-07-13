N, L, R = map(int , input().split())

"""
1≤N≤100
0≤L<R≤23
をチェックしたい
"""

# num = 0 ・・・これは番組を見れる人数
num = 0

if 1 <= N <= 100 and 0 <= L < R <= 23:
    # 条件突破
    for i in range(N):
        Li, Ri = map(int, input().split())
        if 0 <= Li < Ri <= 23:
            if Li <= L and R <= Ri:
                # 条件を満たす場合
                num += 1
                #print(Li, Ri)
    print(num)
    # 条件を満たす人数を出力