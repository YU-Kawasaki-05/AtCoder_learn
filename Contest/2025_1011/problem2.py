"""
def add_kakuketa(n):
    total = sum(int(digit) for digit in n)
    return total

def sigma(n):
    sum = 1
    for i in range(2,n):
        sum += add_kakuketa(i)
    return sum

N = input()
print(sigma(N))
"""




def f(x: int) -> int:
    s = str(x)

    total = sum(int(digit) for digit in s)
    return total

def calculate_a_n(N: int) -> int:
    if N == 0:
        return 1
    
    """
    
    A_n を計算する。
    A_i の値は A[i] に格納される。

    
    """

    A = [1]

    A_1 = f(A[0])
    A.append(A_1)

    for i in range (2,N+1):
        A_prev = A[i-1]
        f_A_prev = f(A_prev)

        A_i = A_prev + f_A_prev
        A.append(A_i)

    return A[N]

# 以下で実行

try:
    N=int(input().strip())
except:
    print("入力が不正です")
    exit()

# 制約：Nは1から100までの整数
if N<1 or N>100:
    print("入力が不正です")
else:
    result = calculate_a_n(N)
    print(result)