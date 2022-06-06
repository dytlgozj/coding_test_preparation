# k번째 수

# 2022-06-06 0136 풀이.

# 정확성 100
# 너무 기본적인 풀이.
def solution(array, commands):
    answer = []

    for i, j, k in commands:
        new_array = array[i - 1:j]
        new_array = sorted(new_array)
        answer.append(new_array[k - 1])
    return answer

# 숏코딩 버전. 람다, 리스트, 맵을 잘 활용하면 이렇게도 짤 수 있다.
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
