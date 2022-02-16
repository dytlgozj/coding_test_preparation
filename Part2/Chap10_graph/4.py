from collections import deque
from copy import copy

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for i in range(1, n + 1):
    one_line = list(map(int, input().split()))
    time[i] = one_line[0]
    prerequisites = one_line[1:-1]
    for j in prerequisites:
        graph[j].append(i)
        indegree[i] += 1

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            # 핵심 로직.
            result[i] = max(result[now] + time[i], result[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n + 1):
        print(result[i])

topology_sort()


# # 입력 예시
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# # 출력 예시
# 10
# 20
# 14
# 18
# 17
