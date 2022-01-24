# 정렬되어 있는 두 리스트를 합집합 하는 알고리즘.
# Merge sort에서 사용함.
# two pointer 기법으로 역시 각각의 리스트의 원소를 가리키는 포인터를 유지하면 된다.

n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] * (n + m)
i = 0
j = 0
k = 0

while i < n or j < m:
    # 리스트 b가 다 처리되었거나, a의 원소가 더 작으면 a꺼를 담음.
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

print(result)
