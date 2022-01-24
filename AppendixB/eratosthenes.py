import math
n = int(input())
array = [True for _ in range(n + 1)]
# 1은 소수가 아니기 때문. 2는 소수가 맞다.
array[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end = " ")
