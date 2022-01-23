# 플로이드 - 워셜 알고리즘. 다익스트라가 한 지점에서 다른 특정 지점까지의 최단 경로 알고리즘이었다면,
# 이 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단경로를 모두 구해야 하는 경우 사용한다.
# 시간복잡도는 O(n^3) 이기 때문에 오래걸린다. 입력 제한 N의 범위를 제대로 파악한 후 적절하게 사용.

INF = int(1e9)

n = int(input())
m = int(input())

# 초기화는 무한대의 값으로.
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 edge는 없을거라 가정하고, 그 부분에 해당하는건 0으로 초기화.
for i in range(1, n + 1):
    graph[i][i] = 0

# edge m개 입력받았으니까, 그걸 그래프에 그대로 반영.
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# Floyd-Warshall Algorithm의 본체. k 루프가 가장 바깥쪽에 존재함에 유의하라.
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 간단한 출력 코드.
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end = " ")
        else:
            print(graph[a][b], end = " ")
    print()


# # 입력 예시
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

# # 출력 예시
# 0 4 8 6
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0
