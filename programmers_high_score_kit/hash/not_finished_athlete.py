# 완주하지 못한 선수

# 2022-06-06 0120 풀이.

# 정확성 50, 효율성 0
# participant에서 하나하나 꺼내서 completion에 있나 없나 확인 후 있으면 지우는 방식.
def solution1(participant, completion):
    answer = ''
    for person in participant:
        if person in completion:
            completion.remove(person)
        elif person not in completion:
            answer = person
    return answer

# 정확성 50, 효율성 50
# 항상 completion이 하나만 적은것이 보장된다는 점을 이용해 정렬해서 푼 방식.
def solution2(participant, completion):
    answer = ''
    part = sorted(participant)
    comp = sorted(completion)

    for i in range(len(comp)):
        if part[i] != comp[i]:
            return part[i]

    return part[-1]

# Counter 객체를 이용한 기상천외한 방법. 카운터 객체끼리 빼기 연산이 된다. -> 반드시 카운터가 1인 것 하나만 남는다.
# 그의 이름을 받아 반환.
import collections

def solution3(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 출제 의도대로 hash 함수를 이용해 푼 방법. 해쉬값을 계속 누적시키면서 더했다가 빼면 남은 그 하나가 바로
# 완주 못한 선수의 hash 값이라는 점을 이용한 방법.
def solution4(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
