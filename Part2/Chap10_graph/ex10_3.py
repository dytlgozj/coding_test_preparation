# 서로소 집합 자료구조를 이용한 크루스칼 알고리즘.
# 시간복잡도는 edge의 갯수를 E라 할 때, O(ElogE). (정렬하는 과정이 가장 크기 때문.)

def find_parent_more_efficient(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_more_efficient(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a, b = find_parent_more_efficient(parent, a), find_parent_more_efficient(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# edge를 비용순으로 정렬시킨다.
edges.sort()

# edge를 하나씩 확인하면서 사이클이 아니면 집합에 포함
for edge in edges:
    cost, a, b = edge
    if find_parent_more_efficient(parent, a) != find_parent_more_efficient(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


# # 입력 예시
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7 
# 4 6 23
# 4 7 13 
# 5 6 53
# 6 7 25

# # 출력 예시
# 159
