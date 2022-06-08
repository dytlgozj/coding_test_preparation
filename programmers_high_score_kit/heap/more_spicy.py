# 더 맵게

# 2022-06-07 0532 풀이.
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        min_scoville = heapq.heappop(scoville)
        min2nd_scoville = heapq.heappop(scoville)
        new_scoville = min_scoville + 2 * min2nd_scoville
        heapq.heappush(scoville, new_scoville)
        answer += 1

        if scoville[0] < K and len(scoville) >= 2:
            continue
        else:
            break
    
    if scoville[0] >= K:
        return answer
    else:
        return -1
