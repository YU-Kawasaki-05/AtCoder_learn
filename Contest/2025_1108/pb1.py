flag = False

X, Y, Z = map(int, input().strip().split())

if not 1 <= X <= 100 or not 1 <= Y <= 100 or not 2 <= Z <= 20:
    exit()


for i in range(1000):
    if(X+i == Z*(Y+i)):
        flag = True
        break

if flag == True:
    print("Yes")
else:
    print("No")