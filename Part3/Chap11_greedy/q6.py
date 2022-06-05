num = int(input())

cnt = 2
a_list = []

while num >= 2:
    if num % cnt == 0:
        num //= cnt
        a_list.append(cnt)
        cnt = 2
    else:
        cnt += 1

