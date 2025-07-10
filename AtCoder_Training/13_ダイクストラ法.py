"""
AtCoder ダイクストラ法問題

問題:
N個の頂点とM本の有向辺からなるグラフがあります。
辺iは頂点A_iから頂点B_iへの長さC_iの有向辺です。
頂点1から頂点Nまでの最短経路長を求めてください。
経路が存在しない場合は-1を出力してください。

入力:
1行目: 頂点数 N と辺数 M
2行目以降: M行にわたり、各辺の情報 A_i B_i C_i

出力:
頂点1から頂点Nまでの最短経路長

制約:
2 <= N <= 10^5
1 <= M <= 2 * 10^5
1 <= A_i, B_i <= N
1 <= C_i <= 10^9

入力例1:
5 7
1 2 2
1 3 5
2 3 1
2 4 4
3 4 2
3 5 6
4 5 3

出力例1:
7
解説: 頂点1→2→3→4→5の経路で長さは2+1+2+3=8

入力例2:
3 2
1 2 5
2 3 8

出力例2:
13
"""

import heapq

def mysolution():
    # 実装を試みてください
    pass

"""
def solve():
    # 入力を受け取る
    N, M = map(int, input().split())
    
    # グラフの作成
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))  # 頂点aから頂点bへのコストcの辺
    
    # ダイクストラ法で最短経路を求める
    def dijkstra(start, goal):
        # 最短距離の初期化
        dist = [float('inf')] * (N + 1)
        dist[start] = 0
        
        # 優先度キュー（最小ヒープ）の初期化
        priority_queue = [(0, start)]  # (距離, 頂点)
        
        while priority_queue:
            # 未確定の頂点の中で最短の頂点を取り出す
            current_dist, current = heapq.heappop(priority_queue)
            
            # 既に処理された頂点は飛ばす
            if current_dist > dist[current]:
                continue
            
            # 隣接する頂点を調べる
            for next_node, cost in graph[current]:
                # より短い経路が見つかった場合は更新
                if dist[next_node] > dist[current] + cost:
                    dist[next_node] = dist[current] + cost
                    heapq.heappush(priority_queue, (dist[next_node], next_node))
        
        # ゴールまでの距離を返す（到達不可能な場合は-1）
        return dist[goal] if dist[goal] != float('inf') else -1
    
    # 頂点1から頂点Nまでの最短経路を計算
    result = dijkstra(1, N)
    print(result)


if __name__ == "__main__":
    solve()
"""
