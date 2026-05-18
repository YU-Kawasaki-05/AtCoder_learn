"""
問題文
以下の 
5 つの日を五節句と呼びます。

1 月 
7 日
3 月 
3 日
5 月 
5 日
7 月 
7 日
9 月 
9 日
M 月 
D 日が五節句に含まれるならば Yes を、含まれないならば No を出力してください。

制約
M,D は整数
M 月 
D 日はグレゴリオ暦における閏年うるうどしの日付として正しい。
入力
入力は以下の形式で標準入力から与えられる。

M 
D
出力
M 月 
D 日が五節句に含まれるならば Yes を、含まれないならば No を出力せよ。

入力例 1
Copy
3 3
出力例 1
Copy
Yes
3 月 
3 日は五節句に含まれるので、Yes を出力します。

入力例 2
Copy
1 1
出力例 2
Copy
No
1 月 
1 日は五節句に含まれないので、No を出力します。

入力例 3
Copy
4 4
出力例 3
Copy
No
入力例 4
Copy
11 7
出力例 4
Copy
No

"""

M, D = map(int, input().strip().split())

if (M == 1 and D == 7) or (M == 3 and D == 3) or (M == 5 and D == 5) or (M == 7 and D == 7) or (M == 9 and D == 9):
    print("Yes")
else:
    print("No")