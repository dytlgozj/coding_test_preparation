# 특정한 합을 가지는 부분 연속 수열 갯수 찾기 문제.
# ex) [1, 2, 3, 2, 5], M = 5 인 경우 -> 3이 출력되어야함.

# 또한, 리스트 내 원소에 음수 데이터가 포함되어 있지 않은 경우만 이 알고리즘을 쓸 수 있다는 점에 유의하라.

n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# start는 0부터 n - 1까지 가고,
for start in range(n):
    # 이 내부에서 end를 옮긴다. 투 포인터 트릭은 구현방법이 여러가지임. 이는 그 중 하나일 뿐이다.
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
