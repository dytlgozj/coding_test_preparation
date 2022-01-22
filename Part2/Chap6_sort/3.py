n = int(input())
array = []

for i in range(n):
    name, score = input().split()
    score = int(score)
    array.append((name, score))

array.sort(key = lambda x: x[1])

for i in range(n):
    print(array[i][0], end = " ")

# # 입력 예시
# 2
# 홍길동 95
# 이순신 77

# # 출력 예시
# 이순신 홍길동
