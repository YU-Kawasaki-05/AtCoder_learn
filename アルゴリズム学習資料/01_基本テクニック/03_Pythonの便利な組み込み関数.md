# Pythonの便利な組み込み関数

競技プログラミングでは、コード量を減らし、可読性を高め、効率的に問題を解くために、Pythonの組み込み関数を活用することが重要です。この資料では、特に競技プログラミングで役立つPythonの組み込み関数を紹介します。

## 1. 数値関連の関数

### 1.1 基本的な数学関数

```python
abs(-5)          # 5 （絶対値）
pow(2, 3)        # 8 （2の3乗）
round(3.14159, 2)  # 3.14 （小数点第2位で四捨五入）
divmod(7, 2)     # (3, 1) （商と余りのタプル）
```

### 1.2 最大値・最小値

```python
max(1, 2, 3, 4)  # 4 （最大値）
min(1, 2, 3, 4)  # 1 （最小値）
max([1, 2, 3, 4])  # 4 （リストの最大値）
```

### 1.3 数値の変換

```python
int('123')        # 123 （文字列から整数へ変換）
float('3.14')     # 3.14 （文字列から浮動小数点へ変換）
int('101', 2)     # 5 （2進数の文字列を10進数に変換）
int('FF', 16)     # 255 （16進数の文字列を10進数に変換）
```

## 2. イテレータ・シーケンス関連の関数

### 2.1 範囲生成と列挙

```python
range(5)            # 0, 1, 2, 3, 4 の範囲を生成
range(2, 5)         # 2, 3, 4 の範囲を生成
range(0, 10, 2)     # 0, 2, 4, 6, 8 の範囲を生成（ステップ2）
enumerate(['a', 'b', 'c'])  # (0, 'a'), (1, 'b'), (2, 'c') のタプルを生成
```

### 2.2 集計関数

```python
sum([1, 2, 3, 4, 5])       # 15 （リストの合計）
all([True, True, False])   # False （すべての要素がTrueか）
any([True, False, False])  # True （いずれかの要素がTrueか）
```

### 2.3 ソートと検索

```python
sorted([3, 1, 4, 1, 5, 9])            # [1, 1, 3, 4, 5, 9]
sorted(['banana', 'apple', 'cherry'])  # ['apple', 'banana', 'cherry']
sorted([3, 1, 4, 1, 5, 9], reverse=True)  # [9, 5, 4, 3, 1, 1]
sorted([(1, 'b'), (2, 'a'), (3, 'c')], key=lambda x: x[1])  # キーでソート
```

### 2.4 マッピングと変換

```python
list(map(int, ['1', '2', '3']))  # [1, 2, 3] （各要素に関数を適用）
list(filter(lambda x: x > 0, [-1, 0, 1, 2]))  # [1, 2] （条件に合う要素のみ）
```

## 3. 文字列関連の関数

### 3.1 文字列の変換

```python
str(123)         # '123' （数値から文字列へ変換）
'Hello'.upper()  # 'HELLO' （大文字に変換）
'Hello'.lower()  # 'hello' （小文字に変換）
```

### 3.2 文字列の操作

```python
', '.join(['apple', 'banana', 'cherry'])  # 'apple, banana, cherry'
'Hello World'.split(' ')                  # ['Hello', 'World']
'  hello  '.strip()                       # 'hello' （前後の空白を削除）
```

## 4. リスト・タプル関連の便利な関数

### 4.1 zip関数

```python
list(zip([1, 2, 3], ['a', 'b', 'c']))  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

### 4.2 リスト内包表記（関数ではないがとても便利）

```python
squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
```

## 5. 集合・辞書関連の関数

```python
set([1, 2, 2, 3, 3, 3])  # {1, 2, 3} （重複を排除）
dict(zip(['a', 'b', 'c'], [1, 2, 3]))  # {'a': 1, 'b': 2, 'c': 3}
```

## 6. 競技プログラミングで特に役立つ関数

### 6.1 itertools モジュール

```python
from itertools import combinations
list(combinations([1, 2, 3, 4], 2))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

from itertools import permutations
list(permutations([1, 2, 3], 2))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from itertools import product
list(product([1, 2], [3, 4]))  # [(1, 3), (1, 4), (2, 3), (2, 4)]

from itertools import accumulate
list(accumulate([1, 2, 3, 4, 5]))  # [1, 3, 6, 10, 15] （累積和）
```

### 6.2 functools モジュール

```python
from functools import reduce
reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 24 （1*2*3*4）

from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

### 6.3 heapq モジュール（優先度付きキュー）

```python
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappop(heap)  # 1 （最小値を取り出し）
```

### 6.4 collections モジュール

```python
from collections import Counter
Counter([1, 1, 2, 2, 2, 3])  # Counter({2: 3, 1: 2, 3: 1}) （要素の出現回数）

from collections import defaultdict
d = defaultdict(int)  # 存在しないキーにアクセスすると0を返す
d['a'] += 1  # d = {'a': 1}

from collections import deque
dq = deque([1, 2, 3])
dq.append(4)       # [1, 2, 3, 4]
dq.appendleft(0)   # [0, 1, 2, 3, 4]
dq.pop()           # 4, dq = [0, 1, 2, 3]
dq.popleft()       # 0, dq = [1, 2, 3]
```

## 7. 実用例：AtCoder問題での活用

### 例1: 入力処理の簡略化

```python
# 複数の整数を一行で読み込む
a, b, c = map(int, input().split())

# 整数のリストを一行で読み込む
numbers = list(map(int, input().split()))

# 複数行の整数をリストに読み込む
n = int(input())
rows = [list(map(int, input().split())) for _ in range(n)]
```

### 例2: グリッド処理の効率化

```python
# 2次元グリッドを扱う問題で、隣接するマスを探索
grid = [list(input()) for _ in range(h)]
dx = [0, 1, 0, -1]  # 上下左右の移動方向
dy = [1, 0, -1, 0]

for x in range(h):
    for y in range(w):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                # 有効な隣接マスの処理
```

### 例3: 二分探索の活用

```python
from bisect import bisect_left, bisect_right

# ソート済みリストでの二分探索
sorted_list = [1, 2, 3, 5, 8, 13, 21]
index = bisect_left(sorted_list, 6)  # 4 （6を挿入すべき位置）

# 値の範囲を二分探索で求める
count = bisect_right(sorted_list, 8) - bisect_left(sorted_list, 8)  # 1 （値8の数）
```

## 8. まとめ

Pythonの組み込み関数やモジュールを適切に活用することで、コードが簡潔になり、実行速度も向上します。競技プログラミングでは、特に以下の点に注目しましょう：

1. 入出力処理の効率化（`map`, `int`, `input`など）
2. データ構造の適切な選択（`list`, `set`, `dict`, `deque`, `heapq`など）
3. イテレーションと変換の効率化（`map`, `filter`, `sorted`など）
4. アルゴリズムの実装簡略化（`itertools`, `functools`など）

これらの組み込み関数を活用することで、より効率的に問題を解決できるようになります。
