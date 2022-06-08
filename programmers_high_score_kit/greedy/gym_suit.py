# 체육복

# 2022-06-07 0324 풀이.

# 정확성 100
def solution1(n, lost, reserve):
    answer = n - len(lost)

    # 정렬되어 들어오지 않는 경우가 있음.
    # 정렬하지 않을 시 테스트 13, 14가 실패함. (why?)

    # lost = [2, 7, 4, 5, 6], reserve = [3, 1] 이면 정렬 안되어 있다. 이경우 lost[0]가 reserve[0]을 가져가서
    # reserve[1]이 쓰이지 못하고 그냥 남게 된다.
    lost = sorted(lost)
    reserve = sorted(reserve)

    # 이렇게 복사로 새로운 리스트로 관리하지 않고 바로 17 line에서 lost.remove() 할 시,
    # 14 for문에 지장이 생긴다. 인덱스가 하나씩 계속 올라가는 도중에 원소가 지워졌기 때문임.
    new_lost = lost.copy()

    for lp in lost:
        if lp in reserve:
            reserve.remove(lp)
            new_lost.remove(lp)
            answer += 1

    for lp in new_lost:
        if lp - 1 in reserve:
            reserve.remove(lp - 1)
            answer += 1

        elif lp + 1 in reserve:
            reserve.remove(lp + 1)
            answer += 1

    return answer

# 참고할만한 풀이법. 특히 리스트를 멋있게 만드는 이 방법은 꼭 알아둬라.
def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
    