# 기능개발

# 2022-06-07 0414 풀이.

from math import ceil

def solution1(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        days.append(ceil((100 - progresses[i]) / speeds[i]))

    while days != []:
        cnt = 1
        norm = days.pop(0)
        while days != [] and norm >= days[0]:
            days.pop(0)
            cnt += 1
        answer.append(cnt)

    return answer

# 반복문을 하나만 쓰고 해결하는 방법. 반드시 익혀둬라.
def solution2(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        tmp = math.ceil((100 - p) / s)
        if len(days) == 0 or days[-1][0] < tmp:
            days.append([tmp, 1])
        else:
            days[-1][1] += 1

    return [day[1] for day in days]
