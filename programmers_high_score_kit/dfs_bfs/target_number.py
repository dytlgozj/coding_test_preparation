# 타겟 넘버

# 2022-06-07 0701 풀이.

# 다시 풀것. 재귀함수로 답을 생각할 수 있는 유연한 사고방식을 갖춰라.
def solution(numbers, target):
    if numbers == []:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return solution(numbers[1:], target + numbers[0]) + solution(numbers[1:], target - numbers[0])

# 파이써닉한 풀이. 잘 익혀라.
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]

    print(f"product(*l) = {list(product(*l))}")
    s = list(map(sum, product(*l)))
    return s.count(target)
