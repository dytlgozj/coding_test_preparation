start = input()

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

result = 0
start_y = ord(start[0]) - ord('a') + 1
start_x = int(start[1])

for mv in range(8):
    nx = start_x + dx[mv]
    ny = start_y + dy[mv]

    if not (nx > 8 or nx < 1 or ny > 8 or ny < 1):
        result += 1

print(result)
