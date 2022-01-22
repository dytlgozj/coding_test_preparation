# 재귀를 이용한 binary_search
def binary_search_recursion(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursion(array, target, start, mid - 1)
    else:
        return binary_search_recursion(array, target, mid + 1, end)

# 반복문을 이용한 binary_search
def binary_search_iterative(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None