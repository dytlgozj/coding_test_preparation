n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input())))

def dfs(x, y):
    if x >= n or x < 0 or y >= m or y < 0 or board[x][y] == 1:
        return False

    board[x][y] = 1
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
    

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
