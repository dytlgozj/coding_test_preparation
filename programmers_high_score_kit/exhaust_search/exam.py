# 가장 큰 수

# 2022-06-06 0230 풀이.

# 정확성 100
# 패턴을 정해두고 모든 정답을 확인하면서 점수 매기는 방법.
def solution(answers):
    answer = []

    pattern = [[1, 2, 3, 4 ,5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    score = [[1, 0], [2, 0], [3, 0]]

    for i in range(len(answers)):
        for j in range(3):
            if pattern[j][i % len(pattern[j])] == answers[i]:
                score[j][1] += 1

    max_score = max([s[1] for s in score])
    for i in range(3):
        if score[i][1] == max_score:
            answer.append(score[i][0])

    return answer
