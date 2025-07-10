"""
AtCoder 幅優先探索(BFS)問題

問題:
H×Wのグリッドがあります。各マスは'.'（通路）か'#'（壁）です。
左上のマス(0,0)からスタートして、右下のマス(H-1,W-1)までの最短距離を求めてください。
上下左右の隣接するマスにのみ移動でき、各移動のコストは1です。

入力:
1行目: H W
2行目以降: H行に渡るグリッドの情報

出力:
最短距離。ゴールにたどり着けない場合は-1を出力。

制約:
1 <= H,W <= 50

入力例1:
3 4
....
.##.
....

出力例1:
6

入力例2:
3 3
...
###
...

出力例2:
-1
"""

from collections import deque

def solve():
    # 入力を受け取る
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    
    # 距離を記録する配列（-1は未訪問）
    dist = [[-1] * W for _ in range(H)]
    
    # 幅優先探索
    queue = deque([(0, 0)])  # スタート位置をキューに入れる
    dist[0][0] = 0  # スタート位置の距離は0
    
    # 移動方向（上下左右）
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        y, x = queue.popleft()
        
        # 上下左右に移動
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            # グリッド内かつ壁でなく未訪問の場合
            if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] == '.' and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))
    
    # 結果出力
    print(dist[H-1][W-1])

if __name__ == "__main__":
    solve()
