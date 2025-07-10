"""
AtCoder セグメント木問題

問題:
長さNの数列A=[A_1, A_2, ..., A_N]があります。
以下の2種類のクエリを処理してください。

1. 1 x v: A_xの値をvに変更する
2. 2 l r: 区間[l, r]の最小値を求める

入力:
1行目: 数列の長さ N とクエリ数 Q
2行目: 数列 A_1, A_2, ..., A_N
3行目以降: Q行のクエリ。各行は「t x v」または「t l r」の形式

出力:
クエリ2に対する回答を各行に出力

制約:
1 <= N, Q <= 10^5
1 <= A_i, v <= 10^9
1 <= l <= r <= N

入力例:
6 7
1 5 3 9 6 7
2 1 5
1 3 7
2 2 6
1 1 4
1 6 2
2 3 5
2 1 6

出力例:
1
3
6
2
"""

def mysolution():
    # 実装を試みてください
    pass

"""
class SegmentTree:
    \"\"\"
    セグメント木の実装
    
    区間に対する操作（最小値、最大値、和など）を効率的に行うデータ構造
    各操作が O(log N) で実行できる
    \"\"\"
    def __init__(self, n, initial_value=float('inf'), operation=min):
        \"\"\"初期化\"\"\"
        # 要素数以上の最小の2のべき乗を計算
        self.n = 1
        while self.n < n:
            self.n *= 2
        
        # セグメント木の配列を初期化
        self.tree = [initial_value] * (2 * self.n - 1)
        self.initial_value = initial_value
        self.operation = operation
    
    def update(self, i, x):
        \"\"\"i番目の要素をxに更新\"\"\"
        # 葉のノードのインデックスを計算
        i += self.n - 1
        # 葉のノードの値を更新
        self.tree[i] = x
        # 親のノードを更新
        while i > 0:
            i = (i - 1) // 2
            self.tree[i] = self.operation(self.tree[2 * i + 1], self.tree[2 * i + 2])
    
    def query(self, a, b, k=0, l=0, r=None):
        \"\"\"区間[a, b)の演算結果を取得\"\"\"
        if r is None:
            r = self.n
        
        # 範囲外なら初期値を返す
        if r <= a or b <= l:
            return self.initial_value
        
        # 範囲内なら現在のノードの値を返す
        if a <= l and r <= b:
            return self.tree[k]
        
        # 左右の子ノードを再帰的に検索
        mid = (l + r) // 2
        vl = self.query(a, b, 2 * k + 1, l, mid)
        vr = self.query(a, b, 2 * k + 2, mid, r)
        return self.operation(vl, vr)

    def build(self, arr):
        \"\"\"配列からセグメント木を構築\"\"\"
        # 葉のノードに値を設定
        for i, val in enumerate(arr):
            self.update(i, val)

def solve():
    # 入力を受け取る
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    # セグメント木の初期化と構築
    seg = SegmentTree(N)
    seg.build(A)
    
    # クエリを処理
    for _ in range(Q):
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            # 更新クエリ
            x, v = query[1], query[2]
            seg.update(x - 1, v)  # 0-indexedに変換
        else:
            # 区間最小値クエリ
            l, r = query[1], query[2]
            print(seg.query(l - 1, r))  # [l, r]を[l-1, r)に変換


if __name__ == \"__main__\":
    solve()
"""
