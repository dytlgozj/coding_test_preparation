n = int(input())
adventurers = list(map(int, input().split()))

result = 0
count = 0

adventurers.sort()

for adventurer in adventurers:
    count += 1
    if count >= adventurer:
        result += 1
        count = 0

print(result)
