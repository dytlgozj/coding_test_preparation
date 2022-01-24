# 구간 합을 구해야 하는 문제가 주어질 때가 있다. [left, right]의 모든 summation을 구하는 문제.
# 이럴때 print(sum(data[left:(right + 1)])) 하면 너무 느리다.
# 보통 O(NM)을 요구 but 이 prefix sum 기법을 이용하면 O(N + M) 시간에 해결할 수 있다.

n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4

print(prefix_sum[right] - prefix_sum[left - 1])
