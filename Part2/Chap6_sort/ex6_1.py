array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# selection sort - 가장 간단.
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]

print(array)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# insertion sort - 이미 데이터가 거의 정렬되어 있는 상태라면 거의 O(N) 시간에 동작.
# 이런 경우는 quick sort 보다 더 빠른 속도를 내기도 함. 반드시 기억.
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
        else:
            break

print(array)


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# quick sort - pivot을 무지성 가장 왼쪽꺼로 선택할 시, 이미 데이터가 거의 정렬되어 있는 상태라면 O(N^2) 시간에 동작.
# 다시 말해, 이미 정렬되어 있는 경우 매우 느리다. 반드시 기억.
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# count sort. O(N + K) 시간에 동작. N은 데이터의 갯수, K는 데이터의 최댓값.
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end =" ")
