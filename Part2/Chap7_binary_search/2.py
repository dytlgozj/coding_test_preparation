# 풀이 1. binary search를 사용한 방법.

import sys
# input = sys.stdin.readline().rstrip()

n = int(input())
component = list(map(int, input().split()))
m = int(input())
wants = list(map(int, input().split()))

component.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for thing in wants:
    if binary_search(component, thing, 0, n - 1) != None:
        print("yes", end = " ")
    else:
        print("no", end = " ")


# 풀이 2. True, False 테이블을 사용한 방법.
n = int(input())
array = [False] * 1000001
for i in input().split():
    array[int(i)] = True

m = int(input())
wants = list(map(int, input().split()))

for thing in wants:
    if array[thing]:
        print("yes", end = " ")
    else:
        print("no", end = " ")


# 풀이 3. set 자료형을 이용하여 아주 효율적으로 찾는 방법.
n = int(input())
myset = set(map(int, input().split()))
m = int(input())
wants = list(map(int, input().split()))

for thing in wants:
    if thing in myset:
        print("yes", end = " ")
    else:
        print("no", end = " ")
