n, m = map(int, input().split())
k = list(map(int, input().split()))

result = 0

for i in range(n - 1):
    count = 0
    for j in range(i + 1, n):
        if k[i] != k[j]:
            count += 1
    result += count

print(result)
