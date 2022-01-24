# 서로소 집합을 활용한 사이클 판별 알고리즘.

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
cycle = False

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    
    if find_parent_more_efficient(parent, a) == find_parent_more_efficient(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
