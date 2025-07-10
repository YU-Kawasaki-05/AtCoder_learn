"""
AtCoder Union-Find問題

問題:
N個の要素からなる集合があります。最初、各要素はそれぞれ独立した集合になっています。
以下のクエリが与えられるので、処理してください：

- unite(x, y): 要素xとyを含む集合を併合する
- same(x, y): 要素xとyが同じ集合に属するかどうかを判定する

入力:
1行目: 要素数 N とクエリ数 Q
2行目以降: Q行のクエリ。各行は「p x y」の形式で与えられる
  - p=0: unite(x, y)
  - p=1: same(x, y)の結果を出力（0: 異なる集合、1: 同じ集合）

出力:
p=1のクエリに対する結果を、各行に出力

制約:
1 <= N, Q <= 10^5
0 <= x, y < N

入力例:
4 7
1 0 1
0 0 1
0 2 3
1 0 1
1 1 2
0 0 2
1 1 3

出力例:
0
1
0
1
"""

class UnionFind:
    """
    Union-Find木（素集合データ構造）の実装
    
    各要素がどの集合に属するかを管理する効率的なデータ構造
    主に以下の操作をサポートする：
    - 要素が属する集合の代表元を見つける（find）
    - 2つの集合を併合する（unite）
    - 2つの要素が同じ集合に属するか判定する（same）
    """
    def __init__(self, n):
        self.parent = list(range(n))  # 親の要素番号を格納（最初は自分自身）
        self.rank = [0] * n  # ランク（木の高さ）を格納
    
    def find(self, x):
        """要素xが属する集合の根（代表元）を見つける"""
        if self.parent[x] == x:
            return x
        else:
            # 経路圧縮: 親を根に更新することで次回の検索を高速化
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    def unite(self, x, y):
        """要素xとyが属する集合を併合する"""
        x_root = self.find(x)
        y_root = self.find(y)
        
        # 既に同じ集合の場合は何もしない
        if x_root == y_root:
            return
        
        # ランク（木の高さ）の低い方を高い方につなぐ
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            # ランクが同じ場合、併合後のランクが1増加
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
    
    def same(self, x, y):
        """要素xとyが同じ集合に属するかを判定する"""
        return self.find(x) == self.find(y)


def solve():
    # 入力を受け取る
    N, Q = map(int, input().split())
    uf = UnionFind(N)
    
    # クエリを処理
    for _ in range(Q):
        p, x, y = map(int, input().split())
        
        if p == 0:
            # uniteクエリ：xとyの集合を併合
            uf.unite(x, y)
        else:
            # sameクエリ：xとyが同じ集合か判定
            print(1 if uf.same(x, y) else 0)


if __name__ == "__main__":
    solve()
"""

def mysolution():
    # 実装を試みてください
    pass
"""
