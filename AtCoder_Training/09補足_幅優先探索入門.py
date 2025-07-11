"""
幅優先探索（BFS）の補足コードと解説

このファイルでは、幅優先探索の基本的な実装例から発展的な問題までを実装します。
初心者が理解しやすいように、探索の各ステップを可視化する関数も用意しています。
"""

from collections import deque
import time

# グリッドの状態を表示する関数
def print_grid(grid, visited=None, current=None, path=None, message=""):
    """グリッドの状態を見やすく表示する補助関数"""
    print(f"--- {message} ---")
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if current and current == (y, x):
                print("C", end="")  # 現在位置
            elif path and (y, x) in path:
                print("*", end="")  # 経路
            elif visited and visited[y][x] >= 0:
                print(visited[y][x] % 10, end="")  # 訪問済み（距離を表示）
            else:
                print(grid[y][x], end="")  # グリッドの元の状態
        print()
    print()

# 1. 基本的なグリッド上のBFS
def grid_bfs_with_visualization(grid, start, goal, delay=0.5):
    """
    グリッド上でBFSを行い、探索の過程を可視化する
    
    Parameters:
    - grid: グリッド（2次元配列）
    - start: スタート位置 (y, x)
    - goal: ゴール位置 (y, x)
    - delay: 表示の遅延時間（秒）
    
    Returns:
    - 最短距離（到達できない場合は-1）
    """
    H, W = len(grid), len(grid[0])
    # 距離を記録する配列（-1は未訪問）
    dist = [[-1] * W for _ in range(H)]
    
    # 幅優先探索
    queue = deque([start])  # スタート位置をキューに入れる
    dist[start[0]][start[1]] = 0  # スタート位置の距離は0
    
    # 移動方向（上下左右）
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dir_names = ["上", "下", "左", "右"]
    
    # 初期状態の表示
    print_grid(grid, dist, start, None, "初期状態")
    if delay: time.sleep(delay)
    
    while queue:
        y, x = queue.popleft()
        current = (y, x)
        
        # 現在位置の表示
        print_grid(grid, dist, current, None, f"現在位置 ({y}, {x}) - 距離: {dist[y][x]}")
        if delay: time.sleep(delay)
        
        # ゴールに到達したら終了
        if (y, x) == goal:
            print(f"ゴール ({goal[0]}, {goal[1]}) に到達しました！最短距離: {dist[y][x]}")
            return dist[y][x]
        
        # 上下左右に移動
        for i, (dy, dx) in enumerate(directions):
            ny, nx = y + dy, x + dx
            
            # グリッド内かつ壁でなく未訪問の場合
            if (0 <= ny < H and 0 <= nx < W and 
                grid[ny][nx] == '.' and dist[ny][nx] == -1):
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))
                print(f"{dir_names[i]}に移動: ({ny}, {nx}) - 距離: {dist[ny][nx]}")
    
    # ゴールに到達できない場合
    print(f"ゴール ({goal[0]}, {goal[1]}) に到達できませんでした。")
    return -1

# 2. 最短経路の復元を行うBFS
def grid_bfs_with_path(grid, start, goal):
    """
    グリッド上でBFSを行い、最短経路も復元する
    
    Returns:
    - (最短距離, 最短経路のリスト)
    """
    H, W = len(grid), len(grid[0])
    dist = [[-1] * W for _ in range(H)]
    prev = [[None] * W for _ in range(H)]  # 経路復元用の配列
    
    queue = deque([start])
    dist[start[0]][start[1]] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        y, x = queue.popleft()
        
        if (y, x) == goal:
            break
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            if (0 <= ny < H and 0 <= nx < W and 
                grid[ny][nx] == '.' and dist[ny][nx] == -1):
                dist[ny][nx] = dist[y][x] + 1
                prev[ny][nx] = (y, x)  # 直前のマスを記録
                queue.append((ny, nx))
    
    # 経路復元
    if dist[goal[0]][goal[1]] == -1:
        return -1, []
    
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = prev[current[0]][current[1]]
    path.append(start)
    path.reverse()  # スタートからゴールの順に並べ直す
    
    return dist[goal[0]][goal[1]], path

# 3. マルチスタートBFS（複数の始点から同時にBFS）
def multi_start_bfs(grid, starts, goal):
    """
    複数のスタート地点から同時にBFSを行う
    
    Parameters:
    - starts: スタート位置のリスト [(y1, x1), (y2, x2), ...]
    
    Returns:
    - 最短距離
    """
    H, W = len(grid), len(grid[0])
    dist = [[-1] * W for _ in range(H)]
    
    queue = deque(starts)
    for y, x in starts:
        dist[y][x] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        y, x = queue.popleft()
        
        if (y, x) == goal:
            return dist[y][x]
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            if (0 <= ny < H and 0 <= nx < W and 
                grid[ny][nx] == '.' and dist[ny][nx] == -1):
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))
    
    return -1

# 4. 状態を拡張したBFS（鍵とドアのある迷路）
def maze_with_key(grid, start, goal, key_pos):
    """
    鍵を拾ってドアを開ける必要がある迷路のBFS
    
    Parameters:
    - grid: グリッド（'.'=通路, '#'=壁, 'D'=ドア）
    - key_pos: 鍵の位置 (y, x)
    
    Returns:
    - 最短距離
    """
    H, W = len(grid), len(grid[0])
    # 状態: (y, x, has_key)
    # has_key: 0=鍵なし, 1=鍵あり
    
    # 訪問状態を記録（3次元配列）
    dist = [[[-1, -1] for _ in range(W)] for _ in range(H)]
    
    queue = deque([(start[0], start[1], 0)])  # スタート時点では鍵を持っていない
    dist[start[0]][start[1]][0] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        y, x, has_key = queue.popleft()
        
        # ゴールに到達したら終了
        if (y, x) == goal:
            return dist[y][x][has_key]
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            # グリッド外なら無視
            if not (0 <= ny < H and 0 <= nx < W):
                continue
                
            new_has_key = has_key
            
            # 鍵を拾った場合
            if (ny, nx) == key_pos:
                new_has_key = 1
                
            # ドアは鍵を持っていないと通れない
            if grid[ny][nx] == 'D' and new_has_key == 0:
                continue
                
            # 壁は通れない
            if grid[ny][nx] == '#':
                continue
                
            # 未訪問の状態なら訪問
            if dist[ny][nx][new_has_key] == -1:
                dist[ny][nx][new_has_key] = dist[y][x][has_key] + 1
                queue.append((ny, nx, new_has_key))
    
    return -1

# 5. 0-1 BFS（辺の重みが0または1の場合）
def zero_one_bfs(grid, start, goal):
    """
    移動コストが0または1の場合のBFS
    
    Parameters:
    - grid: グリッド（'.'=通常マス（コスト1）, '*'=ワープマス（コスト0））
    
    Returns:
    - 最小コスト
    """
    H, W = len(grid), len(grid[0])
    dist = [[-1] * W for _ in range(H)]
    
    # dequeを使用（両端からの挿入・削除が可能）
    queue = deque([start])
    dist[start[0]][start[1]] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        y, x = queue.popleft()
        
        # キューから取り出した後に距離をチェック（他の経路でより短い距離が見つかっている可能性）
        if (y, x) == goal:
            return dist[y][x]
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            if not (0 <= ny < H and 0 <= nx < W) or grid[ny][nx] == '#':
                continue
                
            # 移動コスト（ワープマスならコスト0、それ以外はコスト1）
            cost = 0 if grid[ny][nx] == '*' else 1
            
            # 未訪問または、より短い経路が見つかった場合
            if dist[ny][nx] == -1 or dist[y][x] + cost < dist[ny][nx]:
                dist[ny][nx] = dist[y][x] + cost
                
                # コスト0の場合はキューの先頭に、コスト1の場合は末尾に追加
                if cost == 0:
                    queue.appendleft((ny, nx))  # 優先的に処理
                else:
                    queue.append((ny, nx))
    
    return -1

# 6. 島の数を数えるBFS
def count_islands(grid):
    """
    グリッド上の島の数を数える
    
    Parameters:
    - grid: グリッド（'.'=海, '#'=陸地）
    
    Returns:
    - 島の数
    """
    H, W = len(grid), len(grid[0])
    visited = [[False] * W for _ in range(H)]
    island_count = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for y in range(H):
        for x in range(W):
            # 未訪問の陸地を見つけたら、BFSで連結した陸地を全て探索
            if grid[y][x] == '#' and not visited[y][x]:
                island_count += 1
                queue = deque([(y, x)])
                visited[y][x] = True
                
                while queue:
                    cy, cx = queue.popleft()
                    
                    for dy, dx in directions:
                        ny, nx = cy + dy, cx + dx
                        
                        if (0 <= ny < H and 0 <= nx < W and 
                            grid[ny][nx] == '#' and not visited[ny][nx]):
                            visited[ny][nx] = True
                            queue.append((ny, nx))
    
    return island_count

# 7. 騎士の移動
def knight_moves(start, goal, board_size=8):
    """
    チェス盤上での騎士の最小移動回数を求める
    
    Parameters:
    - start: 開始位置 (y, x)
    - goal: 目標位置 (y, x)
    - board_size: チェス盤のサイズ
    
    Returns:
    - 最小移動回数
    """
    # 訪問状態を記録
    dist = [[-1] * board_size for _ in range(board_size)]
    
    queue = deque([start])
    dist[start[0]][start[1]] = 0
    
    # 騎士の移動方向（8方向）
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    while queue:
        y, x = queue.popleft()
        
        if (y, x) == goal:
            return dist[y][x]
        
        for dy, dx in knight_moves:
            ny, nx = y + dy, x + dx
            
            if (0 <= ny < board_size and 0 <= nx < board_size and 
                dist[ny][nx] == -1):
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))
    
    return -1

# 実行例
if __name__ == "__main__":
    print("==== 基本的なグリッド上のBFS ====")
    grid = [
        '....',
        '.##.',
        '....'
    ]
    start = (0, 0)
    goal = (2, 3)
    
    print("グリッドの内容:")
    for row in grid:
        print(row)
    print(f"スタート: {start}, ゴール: {goal}")
    
    # 視覚化付きのBFSを実行（実際の遅延時間は短く設定）
    grid_bfs_with_visualization(grid, start, goal, delay=0.2)
    
    print("\n==== 最短経路の復元 ====")
    distance, path = grid_bfs_with_path(grid, start, goal)
    print(f"最短距離: {distance}")
    print(f"最短経路: {path}")
    
    # パスを表示
    print_grid(grid, None, None, path, "最短経路")
    
    print("\n==== 島の数え上げ ====")
    island_grid = [
        '.#..#',
        '.#...',
        '.....',
        '#...#',
        '.#...'
    ]
    print("グリッドの内容:")
    for row in island_grid:
        print(row)
    
    island_count = count_islands(island_grid)
    print(f"島の数: {island_count}")
    
    print("\n==== 騎士の移動 ====")
    knight_start = (0, 0)
    knight_goal = (7, 7)
    moves = knight_moves(knight_start, knight_goal)
    print(f"({knight_start[0]}, {knight_start[1]})から({knight_goal[0]}, {knight_goal[1]})までの最小移動回数: {moves}")
