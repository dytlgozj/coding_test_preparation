from collections import deque

n, m = map(int, input().split())

board = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    board.append(list(map(int, input())))
    
def bfs():
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 0:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))
    return board[n - 1][m - 1]

result = bfs()

print(result)
# print()

# for i in range(n):
#     for j in range(m):
#         print(board[i][j], end="")
#     print()
