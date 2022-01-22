n, m = map(int, input().split())

board_visited = [[False] * m for _ in range(n)]
x, y, cur_direction = map(int, input().split())
board_visited[x][y] = True

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 북 동 남 서 순임.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global cur_direction
    cur_direction -= 1
    if cur_direction == -1:
        cur_direction = 3

count = 1
turn_count = 0

while True:
    turn_left()
    nx = x + dx[cur_direction]
    ny = y + dy[cur_direction]

    if board[nx][ny] == 0 and (not board_visited[nx][ny]):
        board_visited[nx][ny] = True
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1
    
    if turn_count == 4:
        nx = x - dx[cur_direction]
        ny = y - dy[cur_direction]
        if board[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_count = 0

print(turn_count)
