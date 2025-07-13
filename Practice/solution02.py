N = int(input())
S = ""  # 空の文字列を初期化
total_length = 0  # 展開後の文字列の総長
enable_output = True  # 出力を有効にするフラグ

for i in range(N):
    txt, li = input().split()
    _li = int(li)  # 文字列を整数に変換
    
    # 長さを加算
    total_length += _li
    
    # 長さが100を超えたら処理終了
    if total_length > 100:
        print("Too Long")
        enable_output = False
        break
    
    # 長さが100以下なら文字列を追加
    S += txt * _li

if enable_output:
    print(S)