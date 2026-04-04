S, A, B, X = map(int, input().split())

if not 1 <= S <= 15 or not 1 <= A <= 1000 or not 1 <= B <= 1000 or not 1 <= X <= 1000:
    print("入力が不正です")
    exit()

distance = int(X/(A+B))*S*A

if X%(A+B) > A:
    distance += A*S
else:
    distance += (X%(A+B))*S

print(distance)