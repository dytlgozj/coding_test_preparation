# 개선된 다익스트라 알고리즘. 노드의 갯수를 V, 엣지의 갯수를 E라 할 때, O(ElogV)의 시간복잡도.
# 이정도 소스코드는 자다가도 갑자기 일어나서 작성 할 수 있을 레벨까지 연습해야함. 숙달 할 것.

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


# # 입력 예시
# 6 11
# 1
# 1 2 2
# 1 3 4
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

# # 출력 예시
# 0
# 2
# 3
# 1
# 2
# 4
