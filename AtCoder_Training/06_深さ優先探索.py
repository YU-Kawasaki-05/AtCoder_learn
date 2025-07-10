"""
AtCoder 深さ優先探索(DFS)問題

問題:
H×Wのグリッドがあります。各マスは'.'（通路）か'#'（壁）です。
左上のマス(0,0)からスタートして、右下のマス(H-1,W-1)にゴールできるか判定してください。
上下左右の隣接するマスにのみ移動できます。

入力:
1行目: H W
2行目以降: H行に渡るグリッドの情報

出力:
ゴールできる場合は"Yes"、できない場合は"No"

制約:
1 <= H,W <= 50

入力例1:
3 4
....
.##.
....

出力例1:
Yes

入力例2:
3 3
...
.#.
.#.

出力例2:
No
"""

def solve():
    # 入力を受け取る
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    
    # 訪問済みを記録する配列
    visited = [[False] * W for _ in range(H)]
    
    # 深さ優先探索
    def dfs(y, x):
        if y < 0 or y >= H or x < 0 or x >= W:
            return False  # グリッド外
        if grid[y][x] == '#':
            return False  # 壁
        if visited[y][x]:
            return False  # 訪問済み
        
        visited[y][x] = True
        
        if y == H - 1 and x == W - 1:
            return True  # ゴール到達
        
        # 上下左右に移動
        return (dfs(y-1, x) or dfs(y+1, x) or 
                dfs(y, x-1) or dfs(y, x+1))
    
    if dfs(0, 0):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()
