"""
深さ優先探索（DFS）の補足コードと解説

このファイルでは、深さ優先探索の基本的な実装例から発展的な問題までを実装します。
初心者が理解しやすいように、探索の過程を可視化する関数も用意しています。
"""

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
            elif visited and visited[y][x]:
                print("o", end="")  # 訪問済み
            else:
                print(grid[y][x], end="")  # グリッドの元の状態
        print()
    print()

# 1. 基本的なグリッド上のDFS（再帰版）
def grid_dfs_recursive(grid, start, goal, visualize=False, delay=0.5):
    """
    グリッド上でDFS（再帰版）を行い、スタートからゴールへの到達可能性を判定
    
    Parameters:
    - grid: グリッド（2次元配列）
    - start: スタート位置 (y, x)
    - goal: ゴール位置 (y, x)
    - visualize: 探索過程を可視化するかどうか
    - delay: 可視化時の遅延時間（秒）
    
    Returns:
    - ゴールに到達可能かどうか
    """
    H, W = len(grid), len(grid[0])
    visited = [[False] * W for _ in range(H)]
    path = []  # 経路を記録
    
    def dfs(y, x):
        # グリッド外、壁、または訪問済みの場合
        if y < 0 or y >= H or x < 0 or x >= W:
            return False
        if grid[y][x] == '#':
            return False
        if visited[y][x]:
            return False
        
        # 訪問済みとマーク
        visited[y][x] = True
        path.append((y, x))
        
        # 可視化
        if visualize:
            print_grid(grid, visited, (y, x), path, f"現在位置 ({y}, {x})")
            if delay: time.sleep(delay)
        
        # ゴールに到達したか
        if (y, x) == goal:
            if visualize:
                print(f"ゴール ({goal[0]}, {goal[1]}) に到達しました！")
            return True
        
        # 上下左右に移動
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dir_names = ["上", "下", "左", "右"]
        
        for i, (dy, dx) in enumerate(directions):
            ny, nx = y + dy, x + dx
            if visualize:
                print(f"{dir_names[i]}に移動を試みます: ({ny}, {nx})")
            
            if dfs(ny, nx):
                return True
        
        # バックトラック（この経路ではゴールに到達できない）
        path.pop()
        if visualize:
            print_grid(grid, visited, None, path, f"バックトラック: ({y}, {x}) から戻ります")
            if delay: time.sleep(delay)
        
        return False
    
    # 初期状態の表示
    if visualize:
        print_grid(grid, None, start, None, "初期状態")
        if delay: time.sleep(delay)
    
    result = dfs(start[0], start[1])
    
    if visualize and result:
        print_grid(grid, None, None, path, "最終経路")
    
    return result

# 2. 基本的なグリッド上のDFS（スタック版）
def grid_dfs_stack(grid, start, goal, visualize=False, delay=0.5):
    """
    グリッド上でDFS（スタック版）を行い、スタートからゴールへの到達可能性を判定
    """
    H, W = len(grid), len(grid[0])
    visited = [[False] * W for _ in range(H)]
    
    stack = [start]
    visited[start[0]][start[1]] = True
    
    # 経路復元用の記録
    prev = {}
    
    # 移動方向（上下左右）
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dir_names = ["上", "下", "左", "右"]
    
    # 初期状態の表示
    if visualize:
        print_grid(grid, visited, start, None, "初期状態")
        if delay: time.sleep(delay)
    
    while stack:
        y, x = stack[-1]  # スタックのトップを見る（まだ取り出さない）
        
        # 可視化
        if visualize:
            path = []
            current = (y, x)
            while current in prev:
                path.append(current)
                current = prev[current]
            path.append(start)
            path.reverse()
            
            print_grid(grid, visited, (y, x), path, f"現在位置 ({y}, {x})")
            if delay: time.sleep(delay)
        
        # ゴールに到達したか
        if (y, x) == goal:
            if visualize:
                path = []
                current = (y, x)
                while current in prev:
                    path.append(current)
                    current = prev[current]
                path.append(start)
                path.reverse()
                
                print(f"ゴール ({goal[0]}, {goal[1]}) に到達しました！")
                print_grid(grid, None, None, path, "最終経路")
            
            return True
        
        # 次に移動できる場所を探す
        found_next = False
        
        for i, (dy, dx) in enumerate(directions):
            ny, nx = y + dy, x + dx
            
            if (0 <= ny < H and 0 <= nx < W and 
                grid[ny][nx] == '.' and not visited[ny][nx]):
                if visualize:
                    print(f"{dir_names[i]}に移動: ({ny}, {nx})")
                
                visited[ny][nx] = True
                stack.append((ny, nx))
                prev[(ny, nx)] = (y, x)
                found_next = True
                break
        
        # 次に進む場所がなければバックトラック（スタックから取り出す）
        if not found_next:
            stack.pop()
            if visualize and stack:
                print(f"バックトラック: ({y}, {x}) から戻ります")
                if delay: time.sleep(delay)
    
    if visualize:
        print(f"ゴール ({goal[0]}, {goal[1]}) に到達できませんでした。")
    
    return False

# 3. 島の数え上げ問題
def count_islands(grid, visualize=False, delay=0.2):
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
    
    def dfs(y, x):
        if y < 0 or y >= H or x < 0 or x >= W:
            return
        if grid[y][x] == '.' or visited[y][x]:
            return
        
        visited[y][x] = True
        
        # 可視化
        if visualize:
            print_grid(grid, visited, (y, x), None, f"島{island_count+1}を探索中: ({y}, {x})")
            if delay: time.sleep(delay)
        
        # 上下左右を探索
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dy, dx in directions:
            dfs(y + dy, x + dx)
    
    # 初期状態の表示
    if visualize:
        print_grid(grid, None, None, None, "初期状態")
        if delay: time.sleep(delay)
    
    for y in range(H):
        for x in range(W):
            if grid[y][x] == '#' and not visited[y][x]:
                island_count += 1
                if visualize:
                    print(f"新しい島（{island_count}個目）を発見: ({y}, {x})")
                dfs(y, x)
    
    if visualize:
        print_grid(grid, visited, None, None, f"探索完了: 合計{island_count}個の島を発見")
    
    return island_count

# 4. 経路の全列挙
def find_all_paths(grid, start, goal, max_paths=10, visualize=False, delay=0.2):
    """
    スタートからゴールまでの全ての経路を列挙
    
    Parameters:
    - grid: グリッド
    - max_paths: 出力する最大経路数（メモリ対策）
    
    Returns:
    - 全経路のリスト
    """
    H, W = len(grid), len(grid[0])
    all_paths = []
    current_path = [start]
    visited = [[False] * W for _ in range(H)]
    
    def dfs(y, x):
        if len(all_paths) >= max_paths:
            return
        
        if (y, x) == goal:
            all_paths.append(current_path.copy())
            if visualize:
                print_grid(grid, None, None, current_path, f"経路{len(all_paths)}を発見")
                if delay: time.sleep(delay)
            return
        
        visited[y][x] = True
        
        # 可視化
        if visualize:
            print_grid(grid, visited, (y, x), current_path, f"探索中: ({y}, {x})")
            if delay: time.sleep(delay)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            if (0 <= ny < H and 0 <= nx < W and 
                grid[ny][nx] == '.' and not visited[ny][nx]):
                current_path.append((ny, nx))
                dfs(ny, nx)
                current_path.pop()  # バックトラック
        
        visited[y][x] = False  # バックトラックのため訪問状態を戻す
    
    visited[start[0]][start[1]] = True
    
    # 初期状態の表示
    if visualize:
        print_grid(grid, visited, start, current_path, "初期状態")
        if delay: time.sleep(delay)
    
    dfs(start[0], start[1])
    
    if visualize:
        print(f"合計{len(all_paths)}個の経路を発見しました。")
    
    return all_paths

# 5. 部分和問題（DFS版）
def subset_sum(nums, target, visualize=False, delay=0.5):
    """
    部分和問題をDFSで解く
    
    Parameters:
    - nums: 整数のリスト
    - target: 目標値
    
    Returns:
    - 部分和が目標値と等しくなる部分集合があるかどうか
    """
    n = len(nums)
    found = False
    current_sum = 0
    selected = []
    
    def visualize_state():
        if not visualize:
            return
        
        print("=" * 40)
        print(f"現在の状態: 合計 = {current_sum}, 目標 = {target}")
        print("選択した要素:", ", ".join(f"{nums[i]}[{i}]" for i in selected))
        print("残りの要素:", ", ".join(f"{nums[i]}[{i}]" for i in range(n) if i not in selected and i > (selected[-1] if selected else -1)))
        print("=" * 40)
        if delay: time.sleep(delay)
    
    def dfs(index, current_sum):
        nonlocal found
        
        # 目標値に到達した場合
        if current_sum == target:
            found = True
            if visualize:
                print("\n🎉 解を発見! 🎉")
                print(f"選択した要素: {[nums[i] for i in selected]}")
                print(f"合計: {current_sum} = 目標値: {target}")
                if delay: time.sleep(delay)
            return True
        
        # 全ての要素を検討し終えた場合
        if index == n:
            return False
        
        visualize_state()
        
        # 現在の要素を選ぶ場合
        selected.append(index)
        if visualize:
            print(f"{nums[index]}[{index}] を選択 → 合計: {current_sum} + {nums[index]} = {current_sum + nums[index]}")
        
        if dfs(index + 1, current_sum + nums[index]):
            return True
        
        # 現在の要素を選ばない場合
        selected.pop()
        if visualize:
            print(f"{nums[index]}[{index}] を選択しない → 合計: {current_sum}")
        
        return dfs(index + 1, current_sum)
    
    if visualize:
        print(f"整数リスト: {nums}")
        print(f"目標値: {target}")
        print("DFSで部分和問題を解きます...")
        if delay: time.sleep(delay)
    
    dfs(0, 0)
    
    if visualize and not found:
        print("\n解が見つかりませんでした。")
    
    return found

# 6. トポロジカルソート（DAG）
def topological_sort(graph, visualize=False, delay=0.5):
    """
    有向非巡回グラフ（DAG）のトポロジカルソートを行う
    
    Parameters:
    - graph: 隣接リスト表現のグラフ {ノード: [隣接ノードのリスト]}
    
    Returns:
    - トポロジカルソート順のノードリスト
    """
    n = len(graph)
    visited = [False] * n
    temp_visited = [False] * n  # サイクル検出用
    order = []
    
    def visualize_state(node, status):
        if not visualize:
            return
        
        print("=" * 40)
        print(f"現在のノード: {node}, 状態: {status}")
        print("訪問済みノード:", ", ".join(str(i) for i in range(n) if visited[i]))
        print("一時訪問中ノード:", ", ".join(str(i) for i in range(n) if temp_visited[i]))
        print("現在のトポロジカル順序:", order[::-1])
        print("グラフ構造:")
        for i in range(n):
            print(f"{i} -> {graph[i]}")
        print("=" * 40)
        if delay: time.sleep(delay)
    
    def dfs(node):
        # サイクル検出
        if temp_visited[node]:
            raise ValueError("グラフにサイクルが存在します。トポロジカルソートは不可能です。")
        
        # 訪問済みならスキップ
        if visited[node]:
            return
        
        visualize_state(node, "訪問開始")
        
        # 一時訪問マーク（サイクル検出用）
        temp_visited[node] = True
        
        # 隣接ノードを探索
        for neighbor in graph[node]:
            dfs(neighbor)
        
        # 訪問完了
        visited[node] = True
        temp_visited[node] = False
        order.append(node)
        
        visualize_state(node, "訪問完了、順序に追加")
    
    if visualize:
        print("トポロジカルソートを実行します...")
        print(f"グラフ: {graph}")
        if delay: time.sleep(delay)
    
    # 全てのノードからDFSを開始
    try:
        for i in range(n):
            if not visited[i]:
                dfs(i)
    except ValueError as e:
        if visualize:
            print(f"エラー: {e}")
        return []
    
    # 逆順にすることでトポロジカルソート順になる
    result = order[::-1]
    
    if visualize:
        print(f"\nトポロジカルソート結果: {result}")
    
    return result

# 実行例
if __name__ == "__main__":
    print("==== 基本的なグリッド上のDFS（再帰版） ====")
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
    
    # 視覚化付きのDFSを実行（実際の遅延時間は短く設定）
    result = grid_dfs_recursive(grid, start, goal, visualize=True, delay=0.2)
    print(f"到達可能: {result}")
    
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
    
    island_count = count_islands(island_grid, visualize=True, delay=0.1)
    print(f"島の数: {island_count}")
    
    print("\n==== 部分和問題 ====")
    nums = [3, 1, 4, 2]
    target = 6
    result = subset_sum(nums, target, visualize=True, delay=0.2)
    print(f"部分和{target}を作れるか: {result}")
    
    print("\n==== トポロジカルソート ====")
    # 有向非巡回グラフの例
    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
        4: []
    }
    result = topological_sort(graph, visualize=True, delay=0.2)
