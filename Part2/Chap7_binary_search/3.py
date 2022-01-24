# 선형 탐색으로 푼 코드. 이는 N과 M의 범위가 너무 크기 때문에 사실상 시간 초과를 받는다.

# n, m = map(int, input().split())
# tteoks = list(map(int, input().split()))

# size = 0
# cutter_height = max(tteoks)

# while size < m:
#     cutter_height -= 1
#     for i in range(n):
#         if (tteok[i] - cutter_height > 0):
#             size += 1

# print(cutter_height)


# 이진 탐색으로 푼 코드. 보통 이렇게 최적화문제를 결정 문제로 환원하여 푸는 기법을 Parametric Search 라고 한다.
# Parametric Search 기법을 이용하여 문제를 풀 경우, 거의 반드시 이진 탐색 코드를 사용한다.
# 여기서는 떡의 길이가 20억 까지의 범위를 가짐을 보고, 바로 이진 탐색을 자연스럽게 떠올릴 수 있어야 했다.

n, m = map(int, input().split())
tteoks = list(map(int, input().split()))

start = 0
end = max(tteoks)
result = 0

while start <= end:
    size = 0
    mid = (start + end) // 2

    for tteok in tteoks:
        if tteok > mid:
            size += tteok - mid
    
    if size < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
