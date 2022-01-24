# 서로소 집합 알고리즘.

# x원소의 '루트'노드 찾는 함수. but, 함수명은 관례적으로 find_parent()라고 한다.
# 이 함수는 매우 기본적인 알고리즘으로 O(V) 시간이 걸림. 최악의 경우 모든 vertex를 뒤진다.
# find_parent_more_efficient() 함수를 쓸것.
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    else:
        return x

# 이 함수는 기존 find_parent()의 비효율성을 개선함. path compression 이라는 기법을 적용한 것임.
# 경로 압축 기법.
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

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합 : ", end = " ")
for i in range(1, v + 1):
    print(find_parent_more_efficient(parent, i), end = " ")

print()

print("부모 테이블 : ", end = " ")
for i in range(1, v + 1):
    print(parent[i], end = " ")


# # 입력 예시
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

# # 출력 예시
# 각 원소가 속한 집합 : 1 1 1 1 5 5
# 부모 테이블 : 1 1 2 1 5 5
