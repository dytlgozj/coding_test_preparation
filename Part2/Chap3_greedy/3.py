n, m = map(int, input().split())
board = []
min_list = []

for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    min_list.append(min(board[i]))

print(max(min_list))
