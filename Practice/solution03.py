A = int(input())
N = int(input())

def convert_to_Ashinhou(n, base):#nをbase進数に変換する関数
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    return ''.join(reversed(digits))

def check_kaibun(str1, str2):
    """
    # 問題点1: この関数は現在値を返していません（return文がない）
    # テストが失敗している原因は、すべての条件をパスしても最後に明示的にTrueを返さないため
    # Noneが返されてしまうことです。
    
    # 問題点2: コメントから推測するに、この関数の目的はstr1の文字とstr2の逆順の文字を
    # 比較することですが、それを回文チェックと呼んでいます。実際には「str1とstr2の逆順が同じか」を
    # チェックしています。
    
    # 問題点3: 全ループを通過した後にTrueを返す必要があります。
    
    # 問題点4: 関数の仕様と命名が曖昧です。check_kaibunという名前から期待されるのは
    # 「文字列が回文かどうか」をチェックすることですが、実際の実装は「str1の文字とstr2の逆順の文字が
    # 一致しているか」をチェックしています。
    """
    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)//2):

        """
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        ↑  合計10個のN
            i=0と9(=10-1)が同じ
            i=1と8(=10-2)が同じ
                    ↑ 10 - i - 1

        """
        if str1[i] != str2[len(str2) - i - 1 ]:
            return False
            
    # 問題点を修正: すべてのチェックをパスしたらTrueを返す
    return True

total = 0

"""
# 問題点5: 現在のコードではN（上限値）が非常に大きい場合に問題があります。
# range(1, N+1)は非常に大きなリストを生成しようとするため、メモリエラーや実行時間の問題が発生します。
# 特にN=10**12の場合、このループは現実的ではありません。

# 問題点6: ループ内で常に「N」を使用していますが、これは「i」を使用すべきです。
# 現在のコードでは毎回同じNに対してチェックしていて、1からNまでの数を検証していません。

# 問題点7: 効率的なアルゴリズムの検討が必要です。回文数は特定のパターンで生成できるため、
# すべての数をチェックする代わりに、直接回文数を生成するアプローチが効率的です。

# 問題点8: 回文の定義の確認が必要です。問題では「10進法とA進法の両方で回文になる数」を
# 求めていますが、現在の実装は「10進法の数とそのA進法表現が逆順の関係にある」数を探しています。
# 本来は「各表現が自身の逆順と同じ（回文である）」数を探すべきです。
"""

# ---------------------------------------------------------------------------
# TLEを回避する効率的なアルゴリズムの提案
# ---------------------------------------------------------------------------
"""
現在の実装では、1からNまでのすべての数に対して、10進法とA進法の両方で回文かどうかをチェックしています。
これはN=10^12のような大きな値に対してはTLE（時間制限超過）が発生します。

効率的なアルゴリズムの提案:

1. 回文数の直接生成:
   - すべての数をチェックする代わりに、10進法の回文数を直接生成します
   - 10進法の回文数は桁数に応じたパターンがあります
     - 1桁: 1, 2, 3, ..., 9
     - 2桁: 11, 22, 33, ..., 99
     - 3桁: 101, 111, 121, ..., 999
     - 4桁: 1001, 1111, 1221, ..., 9999
     - など

2. 生成した10進法の回文数に対してのみA進法変換とチェックを行う:
   - 10進法で回文でない数はスキップできるので、チェック数が大幅に減少します
   - 10進法の回文数は、N以下の全数字の中のごく一部です（O(√N)程度）

3. 桁数ごとの処理:
   - 1桁: [1-9]
   - 2桁: [11,22,...,99]
   - 3桁: 外側の数字を決定し、中央の数字を0-9で試す
   - 4桁以上: 外側から内側へ向かって数字を決定していく

実装例（疑似コード）:

```python
def generate_decimal_palindromes(max_n):
    palindromes = []
    
    # 1桁の回文数
    for i in range(1, 10):
        if i <= max_n:
            palindromes.append(i)
    
    # 2桁以上の回文数を生成
    for length in range(2, len(str(max_n)) + 1):
        # 奇数桁の場合
        if length % 2 == 1:
            for outer in range(10**(length//2), 10**(length//2 + 1)):
                outer_str = str(outer)
                palindrome_str = outer_str + outer_str[:-1][::-1]
                palindrome = int(palindrome_str)
                if palindrome <= max_n:
                    palindromes.append(palindrome)
        # 偶数桁の場合
        else:
            for outer in range(10**(length//2 - 1), 10**(length//2)):
                outer_str = str(outer)
                palindrome_str = outer_str + outer_str[::-1]
                palindrome = int(palindrome_str)
                if palindrome <= max_n:
                    palindromes.append(palindrome)
    
    return palindromes

def solve_efficiently(A, N):
    total = 0
    # 10進法の回文数を生成
    decimal_palindromes = generate_decimal_palindromes(N)
    
    # 各回文数に対してA進法での回文チェック
    for num in decimal_palindromes:
        base_a_repr = convert_to_Ashinhou(num, A)
        if base_a_repr == base_a_repr[::-1]:  # A進法でも回文か
            total += num
            
    return total
```

この改善策の時間計算量は約O(√N)となり、N=10^12の場合でも十分高速に動作します。
10進法の回文数の数はO(√N)程度しかないため、チェックする数が大幅に減少します。

追加の最適化ポイント:
1. メモリ効率向上のため、リストに格納せずジェネレータパターンを使用することも可能
2. 生成済みの回文数をA進法に変換する前にフィルタリングすることで、変換処理も減らせます
3. 特定の桁数のパターンをさらに効率化することも可能です
"""

# 実装例（実際の効率的な解決策）
def generate_palindrome_numbers(max_n):
    """10進法での回文数を生成するジェネレータ関数"""
    # 1桁の回文数
    for i in range(1, min(10, max_n + 1)):
        yield i
    
    # 2桁以上の回文数
    digits = 1
    while True:
        # 次の桁数の最小値を計算
        min_value = 10**digits
        if min_value > max_n:
            break
            
        # 偶数桁の場合
        for prefix in range(10**(digits), 10**(digits + 1)):
            # プレフィックスから回文を生成
            palindrome_str = str(prefix) + str(prefix)[::-1]
            palindrome = int(palindrome_str)
            if palindrome > max_n:
                break
            yield palindrome
            
        # 奇数桁の場合
        for prefix in range(10**(digits), 10**(digits + 1)):
            for middle in range(10):
                # プレフィックス + 中間の数字 + 逆順プレフィックス
                palindrome_str = str(prefix) + str(middle) + str(prefix)[::-1]
                palindrome = int(palindrome_str)
                if palindrome > max_n:
                    break
                yield palindrome
        
        digits += 1

def efficient_solution(A, N):
    """効率的な解決策のメイン関数"""
    if not (2 <= A <= 9 and 1 <= N <= 10**12):
        return 0
        
    total = 0
    for num in generate_palindrome_numbers(N):
        base_a_repr = convert_to_Ashinhou(num, A)
        if base_a_repr == base_a_repr[::-1]:
            total += num
            
    return total

# 実行コード例（コメントアウトされています）
"""
# コメントを外すと効率的なアルゴリズムで実行されます
if __name__ == "__main__":
    A = int(input())
    N = int(input())
    print(efficient_solution(A, N))
"""

