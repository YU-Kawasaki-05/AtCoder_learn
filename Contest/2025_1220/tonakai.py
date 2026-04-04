T = int(input().strip())

N = [0]*T

for i in range(T):
    N[i] = int(input().strip())
    total = 0
    tonakais = [list(map(int, input().split())) for _ in range(N[i])]
    tonakais.sort(key=lambda x: x[1], reverse=True)

    for k in range(N[i]):
        sumP = sum([tonakais[m][1] for m in range(k)])
        sumW = sum([tonakais[m][0] for m in range(k)])
        if sumP >= sumW:
            total = k + 1
            break
    
    print(" "+str(total))