A, B = map(int, input().strip().split())

if not 1 <= A <= 8 or not 0 <= B <= 11:
    exit()
else:
    print(str(A*12 + B))