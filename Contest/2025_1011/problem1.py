"""
問題文
英大文字からなる文字列 
S が与えられます。ここで、
S の長さは奇数です。

S の中央の文字を削除して得られる文字列を出力してください。ただし、
S の中央の文字とは 
S の長さを 
L として 
S の デックス計算
2
L+1
​
  文字目の文字を指します。

制約
S は英大文字からなる文字列
S の長さは 
3 以上 
9 以下の奇数
"""

"""
設計:
- Sを入力される
- Sの長さを取得
- Sの(L+1)/2番目の文字を削除
- 残りの文字列を出力
"""

S = input()
length = len(S)
middle_index = (length + 1) // 2 - 1  # 0-indexedの場合

chars = list(S)
chars.pop(middle_index)

result="".join(chars)
print(result)