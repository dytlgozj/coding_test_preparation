from shutil import move


n = int(input())
plans = input().split()

cur_x = 1
cur_y = 1

move_types = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for mv_typ in range(len(move_types)):
        if plan == move_types[mv_typ]:
            next_x = cur_x + dx[mv_typ]
            next_y = cur_y + dy[mv_typ]
    
    if next_x < 1 or next_x > n or next_y < 1 or next_y > n:
        continue
    
    cur_x, cur_y = next_x, next_y

print(cur_x, cur_y)
